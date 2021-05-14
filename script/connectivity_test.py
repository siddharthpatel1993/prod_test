import subprocess
import re
import time

rel_name="may12"

def copy_config():

    # Using readlines()
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
        subprocess.check_output("mkdir -p ~/."+ rel_name +"", shell=True)
        subprocess.check_output("cp "+ a1 +" ~/."+ rel_name +"", shell=True)
    main_func()

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
    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())
        #print(a1)

        s0 = re.compile(r'/[a-z]+[.][a-z]+')
        m0 = s0.search(a1)
        print(m0.group())
        a0=m0.group().lstrip('/')

        print("******Works start**********")
        print("Showing the difference between "+ a1 +" and ~/.may12/"+ a0 +"")
        subprocess.call("diff "+ a1 +" ~/."+ rel_name +"/"+ a0 +"", shell=True)
        print("******Done*********")
        time.sleep(3)

    print("********Completed the Work***********")
    main_func()

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

def main_func():
    print('''enter 1 to copy the config files
enter 2 to stop the service
enter 3 to deploy the service
enter 4 to compare the config files
enter 5 see the checksum if that is ok
enter 6 to start the app
enter 7 check the alarm
enter 8 to notify everyone throgh email''')
    a = int(input())
    if (a==1):
        copy_config()
    elif(a==2):
        stop_service()
    elif(a==3):
        deploy_service()
    elif(a==4):
        compare_config()
    elif(a==5):
        check_checksum() 
    elif(a==6):
        start_service()
    elif(a==7):
        check_alarm()
    elif(a==8):
        Notify_everyone()
    else:
        print("Wrong choice")
        #break

main_func()

