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

def stop_service():
    subprocess.call("service apache2 stop", shell=True)
    subprocess.call("service apache2 status", shell=True)

def deploy_service():


def url_service_function1():

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

def url_service_function2():

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

        subprocess.check_output("cp "+ a1 +" .config/", shell=True)

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
    url_service_function()
elif(a==2):
    url_service_function1()
else:
    print("Wrong choice")

