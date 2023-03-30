import subprocess
import re
import time

def copy_osconfig():
    global rel_name
    # Using readlines()
    file1 = open('configuration_and_log/configuration_os.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    rel_name = input("Enter the release name\n")
    #Strips the newline character
    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())

        s0 = re.compile(r'.*[,]')
        m0 = s0.search(a1)
        command=m0.group().rstrip(',')

        s1 = re.compile(r'[,][a-zA-Z_.]+')
        m1 = s1.search(a1)
        file=m1.group().lstrip(',')

        subprocess.check_output("mkdir -p $PWD/.siddos/"+ rel_name +"", shell=True)
        subprocess.run(""+ command +" 2>/dev/null >> $PWD/.siddos/"+ rel_name +"/"+file+"", shell=True)


def copy_appconfig():
    global rel_name
    # Using readlines()
    file1 = open('configuration_and_log/configuration_app.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    rel_name = input("Enter the release name\n")
    #Strips the newline character
    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())

        s0 = re.compile(r'.*[,]')
        m0 = s0.search(a1)
        command=m0.group().rstrip(',')
        
        s1 = re.compile(r'[,][a-z1-9A-Z_.]+')
        m1 = s1.search(a1)
        file=m1.group().lstrip(',')

        subprocess.check_output("mkdir -p $PWD/.siddapp/"+ rel_name +"", shell=True)
        subprocess.run(""+ command +" 2>/dev/null >> $PWD/.siddapp/"+ rel_name +"/"+file+"", shell=True)


def stop_service():
    subprocess.call("service apache2 stop", shell=True)
    subprocess.call("service apache2 status", shell=True)
    main_func()

def deploy_service():
    file1 = open('configuration_and_log/configuration.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #Strips the newline character
    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())
        #print(a1)

        s0 = re.compile(r'/[a-z]+[.][a-z]+')
        m0 = s0.search(a1)
        #print(m0.group())
        a0=m0.group().lstrip('/')

        print("******Works start**********")
        print("Copying ../main_conf/"+ a0 +" and "+ a1 +"")
        subprocess.check_output("cp ../main_conf/"+ a0 +" "+ a1 +"", shell=True)
        print("******Done*********")
        time.sleep(3)
    print("*****Completed*****")
    main_func()

def compare_osconfig():
    x = subprocess.check_output("cat configuration_and_log/configuration_os.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > configuration_and_log/configuration1_os.txt", shell=True)
    
    # Using readlines()
    file1 = open('configuration_and_log/configuration1_os.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #Strips the newline character

    b1 = input("enter the first dir\n")
    b2 = input("enter the second dir\n")

    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())

        s1 = re.compile(r'[,][a-zA-Z_.]+')
        m1 = s1.search(a1)
        file=m1.group().lstrip(',')

        print("******Works start**********")
        print("Showing the difference between $PWD/.siddos/"+ b1 +"/"+ file +"  and $PWD/.siddos/"+ b2 +"/"+ file +"")
        subprocess.call("diff $PWD/.siddos/"+ b1 +"/"+ file +" $PWD/.siddos/"+ b2 +"/"+ file +"", shell=True)
        subprocess.check_output("rm -rf configuration_and_log/configuration1_os.txt", shell=True)
        print("******Done*********")
        #time.sleep(3)

    print("********Completed the Work***********")

def compare_appconfig():
    x = subprocess.check_output("cat configuration_and_log/configuration_app.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > configuration_and_log/configuration1_app.txt", shell=True)

    # Using readlines()
    file1 = open('configuration_and_log/configuration1_app.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #Strips the newline character

    b1 = input("enter the first dir\n")
    b2 = input("enter the second dir\n")

    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())

        s1 = re.compile(r'[,][a-zA-Z_.1-9]+')
        m1 = s1.search(a1)
        file=m1.group().lstrip(',')

        print("******Works start**********")
        print("Showing the difference between /home/siddapp/"+ b1 +"/"+ file +"  and /home/siddapp/"+ b2 +"/"+ file +"")
        subprocess.call("diff $PWD/.siddapp/"+ b1 +"/"+ file +" $PWD/.siddapp/"+ b2 +"/"+ file +"", shell=True)
        subprocess.check_output("rm -rf configuration_and_log/configuration1_app.txt", shell=True)
        print("******Done*********")
        #time.sleep(3)

    print("********Completed the Work***********")

def check_checksum():
    main_func()

def start_service():
    subprocess.call("service apache2 start", shell=True)
    subprocess.call("service apache2 status", shell=True)
    main_func()

def check_alarm():
    a = subprocess.call("grep -i -E 'error|alarm' /var/log/apache2/error.log", shell=True)
    print(a)
    main_func()

def Notify_everyone():
    main_func()

def service_status():
    a = subprocess.check_output("ps -ef | grep -i apache2 | grep -v grep | wc -l", shell=True)

    if (int(a)==3):
        print("All processes are up and running")
    else:
        print("Apache is not running")

    main_func()

def main_func():
    print("*****main option starts******")
    print('''enter 1 to copy the OS releated config files
enter 2 to copy the app releated config files
enter 3 to stop the service
enter 4 to deploy the service
enter 5 to compare the os config files
enter 6 to compare the app config files
enter 7 see the checksum if that is ok
enter 8 to start the app
enter 9 check the alarm
enter 10 to notify everyone through email
enter 11 to check the status
enter 12 for connectivity test
enter other than 1-12 to exit''')
    print("*******main option ends********")
    a = input()
    if (a=='1'):
        copy_osconfig()
    elif(a=='2'):
        copy_appconfig()
    elif (a=='3'):
        stop_service()
    elif(a=='4'):
        deploy_service()
    elif(a=='5'):
        compare_osconfig()
    elif (a=='6'):
        compare_appconfig()
    elif(a=='7'):
        check_checksum()
    elif(a=='8'):
        start_service()
    elif(a=='9'):
        check_alarm()
    elif(a=='10'):
        Notify_everyone()
    elif(a=='11'):
        service_status()
    else:
        print("Exiting...")
        #break

main_func()
