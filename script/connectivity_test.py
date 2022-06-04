import subprocess
import re
import time

def copy_config():
    global rel_name
    # Using readlines()
    file1 = open('../configuration_and_log/configuration.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    rel_name = input("Enter the release name\n")
    #Strips the newline character
    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())
        #print(a1)
        subprocess.check_output("mkdir -p /home/"+ rel_name +"", shell=True)
        subprocess.check_output("cp /sys/fs/cgroup/"+ a1 +" /home/"+ rel_name +"", shell=True)

def stop_service():
    subprocess.call("service apache2 stop", shell=True)
    subprocess.call("service apache2 status", shell=True)
    main_func()

def deploy_service():
    file1 = open('../configuration_and_log/configuration.txt', 'r')
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

def compare_config():
    # Using readlines()
    file1 = open('../configuration_and_log/configuration.txt', 'r')
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
        #print(a1)

        #s0 = re.compile(r'/[a-z]+[.][a-z]+')
        #m0 = s0.search(a1)
        #print(m0.group())
        #a0=m0.group().lstrip('/')

        print("******Works start**********")
        print("Showing the difference between /home/"+ b1 +"/"+ a1 +"  and /home/"+ b2 +"/"+ a1 +"")
        subprocess.call("diff /home/"+ b1 +"/"+ a1 +" /home/"+ b2 +"/"+ a1 +"", shell=True)
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

    if (int(a)==4):
        print("All processes are up and running")
    else:
        print("Apache is not running")

    main_func()

def main_func():
    print("*****main option starts******")
    print('''enter 1 to copy the config files
enter 2 to stop the service
enter 3 to deploy the service
enter 4 to compare the config files
enter 5 see the checksum if that is ok
enter 6 to start the app
enter 7 check the alarm
enter 8 to notify everyone through email
enter 9 to check the status
enter other than 1-9 to exit''')
    print("*******main option ends********")
    a = input()
    if (a=='1'):
        copy_config()
    elif(a=='2'):
        stop_service()
    elif(a=='3'):
        deploy_service()
    elif(a=='4'):
        compare_config()
    elif(a=='5'):
        check_checksum()
    elif(a=='6'):
        start_service()
    elif(a=='7'):
        check_alarm()
    elif(a=='8'):
        Notify_everyone()
    elif(a=='9'):
        service_status()
    else:
        print("Exiting...")
        #break

main_func()
