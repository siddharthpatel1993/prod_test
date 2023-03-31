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

def connectivity_test():

    def url_service_function():
        x = subprocess.check_output("cat configuration_and_log/configuration_url_service.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > configuration_and_log/configuration.txt", shell=True)
    
        # Using readlines()
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
    
            s0 = re.compile(r'^[A-Za-z-0-9_ ]+[=]')
            m0 = s0.search(a1)
            if m0:
                service_name = m0.group()
                print("Service Name ==> "+ service_name.rstrip('=') +"")
            s1 = re.compile(r'[/][/](.*)[/]')
            m1 = s1.search(a1)
            #print(m1.group(1))
            if m1:
                #print(m1.group(1))
                a2 = m1.group(1)
                s2 = re.compile(r'(.*)[:](.*)')
                m2 = s2.search(a2)
                #print(m2.group(0))
                if m2:
                    #print(m2.group(0))
                    a3 = m2.group(0)
                    #print(m2.group(0))
                    s3 = re.compile(r'(.*)[:]')
                    m3 = s3.search(a3)
                    host = m3.group(1)
                    print("Host "+ str(host_num) +" ==> "+ host +"")
                    s4 = re.compile(r'[:][0-9]+')
                    m4 = s4.search(a3)
                    port = m4.group().strip(':')
                    print("Port ==> "+ port +"")
                    y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
    
                else:
                    s5 = re.compile(r'[/][/](.*)[/]')
                    m5 = s5.search(a1)
                    s6 = re.compile(r'[/][/][a-z0-9]+[.][a-z]+[.][a-z]+')
                    m6 = s6.search(a1)
                    if m6:
                        #print(m5.group())
                        host = m6.group().lstrip('//')
                        print("Host "+ str(host_num) +" ==> "+ host +"")
                        s7 = re.compile(r'[=](.*)[:]')
                        m7 = s7.search(a1)
                        #print(m5.group(1))
                        a5 = m7.group(1).lstrip()
                        if (a5 == 'http'):
                            print("As it is http, and port is not mentioned so using default port 80")
                            port = '80'
                            print("Port ==> "+ port +"")
                            y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                            print("********************Done****************")
                            time.sleep(3)
                            continue
                        elif(a5 == 'https'):
                            print("As it is https, and port is not mentioned so using default port 443")
                            port = '443'
                            print("Port ==> "+ port +"")
                            y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                            print("********************Done****************")
                            time.sleep(3)
                            continue
                        else:
                            print("It is neither http not https")
                            print("********************Done****************")
                            time.sleep(3)
                            continue
                    if m5:
                        host1 = m5.group(1)
                        s8 = re.compile(r'^[A-Za-z0-9.-]+')
                        m8 = s8.search(host1)
                        host = m8.group()
                        print("Host "+ str(host_num) +" ==> "+ host +"")
                        s9 = re.compile(r'[=](.*)[:]')
                        m9 = s9.search(a1)
                        #print(m9.group(1))
                        a5 = m9.group(1).lstrip()
                        if (a5 == 'http'):
                            print("As it is http, and port is not mentioned so using default port 80")
                            port = '80'
                            print("Port ==> "+ port +"")
                            y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                            print("********************Done****************")
                            time.sleep(3)
                            continue
                        elif(a5 == 'https'):
                            print("As it is https, and port is not mentioned so using default port 443")
                            port = '443'
                            print("Port ==> "+ port +"")
                            y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                            print("********************Done****************")
                            time.sleep(3)
                            continue
    
                        print("********************Done****************")
                        time.sleep(3)
                        continue
    
                print("********************Done****************")
                time.sleep(3)
    
            else:
                #print(a1)
                s10 = re.compile(r'[/][/](.*)[:](.*)')
                m10 = s10.search(a1)
                if m10:
                    fqdn = m10.group()
                    #print(fqdn)
                    s11 = re.compile(r'[/][/](.*)[:](.*)')
                    m11 = s11.search(fqdn)
                    host = m11.group(1)
                    print("Host "+ str(host_num) +" ==> "+ host +"")
                    s12 = re.compile(r'[:](.*)')
                    m12 = s12.search(fqdn)
                    port = m12.group(1)
                    print("Port ==> "+ port +"")
                    y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                    print("********************Done****************")
                    time.sleep(3)
                    continue
    
                s13 = re.compile(r'[/][/](.*)')
                m13 = s13.search(a1)
                if m13:
                    host = m13.group(1)
                    print("Host "+ str(host_num) +" ==> "+ host +"")
                    s14 = re.compile(r'[=](.*)[:]')
                    m14 = s14.search(a1)
                    #print(m14.group(1))
                    a5 = m14.group(1).lstrip()
                    if (a5 == 'http'):
                        print("As it is http, and port is not mentioned so using default port 80")
                        port = '80'
                        print("Port ==> "+ port +"")
                        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                        print("********************Done****************")
                        time.sleep(3)
                        continue
                    elif(a5 == 'https'):
                        print("As it is https, and port is not mentioned so using default port 443")
                        port = '443'
                        print("Port ==> "+ port +"")
                        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                        print("********************Done****************")
                        time.sleep(3)
                        continue
    
                s15 = re.compile(r'=(.*)')
                m15 = s15.search(a1)
                if m15:
                    host = m15.group(1)
                    print("Host "+ str(host_num) +" ==> "+ host +"")
                    port = '25'
                    print("Port ==> "+ port +"")
                    y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                    print("********************Done****************")
                    time.sleep(3)
                    continue
    
        subprocess.check_output("rm -rf configuration_and_log/configuration.txt", shell=True)
        print("********************Completed****************")
    
    def manual_change_function():
        x = subprocess.check_output("cat configuration_and_log/configuration_manual_change.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > configuration_and_log/configuration1.txt", shell=True)
    
        # Using readlines()
        file2 = open('configuration_and_log/configuration1.txt', 'r')
        Lines = file2.readlines()
        file2.close()
    
        count = 0
        #Strips the newline character
        for line in Lines:
            count = count + 1
            host_num = count
    
            a2 = "{}".format(line.strip())
            #print(a2)
    
            s0 = re.compile(r'^[a-zA-Z0-9_]+,')
            m0 = s0.search(a2)
            service_name = m0.group().rstrip(',')
            print("Service Name ==> "+ service_name +"")
    
            s1 = re.compile(r'[,][a-zA-Z0-9_.-]+[:]')
            m1 = s1.search(a2)
    
            host= (m1.group(0).rstrip(':')).lstrip(',')
            print("Host "+ str(host_num) +" ==> "+ host +"")
    
            s2 = re.compile(r'[:][0-9]+')
            m2 = s2.search(a2)
            port = m2.group().lstrip(':')
            print("Port ==> "+ port +"")
    
            y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
    
            print("********************Done****************")
            time.sleep(3)
    
        subprocess.check_output("rm -rf configuration_and_log/configuration1.txt", shell=True)
        print("********************Completed****************")

    def manual_input():
        n = int(input("Enter the number of servers you have for test\n"))
        print("*****************Checking the connection starts****************")
    
        for i in range (n):
            count = i + 1
            host = str(input("Enter the "+ str(count) +" host\n"))
            port = str(input("Enter the port\n"))
    
            y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
    
            print("********************Done****************")
    
        print("********************Completed****************")

    print('''Press 1 for URL service type connectivity test
Press 2 for Manual configuration type connectivity test
Press 3 for giving input of host and port from keyboard everytime''')
    option = int(input())
    if( option == 1 ):
        print("*****************Checking the connection starts****************")
        url_service_function()
    elif( option == 2 ):
        print("*****************Checking the connection starts****************")
        manual_change_function()
    elif( option == 3 ):
        print("*****************Checking the connection starts****************")
        manual_input()
    else:
        print("You gave wrong choice, pls give right input")


if __name__=="__main__":
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
    elif(a=='12'):
        connectivity_test()
    else:
        print("Exiting...")
        #break
