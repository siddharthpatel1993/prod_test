import subprocess
import re
import time

def url_service_function():

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
        subprocess.check_output("mkdir -p ~/."+ rel_name +"", shell=True)
        subprocess.check_output("cp "+ a1 +" ~/."+ rel_name +"", shell=True)

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

        s0 = re.compile(r'/[a-z]+.[a-z]+')
        m0 = s0.search(a1)
        a0=m0.group().lstrip('/')

        print("******Works start**********")
        print("Showing the difference between "+ a1 +" and ~/.may12/"+ a0 +"")
        subprocess.call("diff "+ a1 +" ~/.may12/"+ a0 +"", shell=True)
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
enter 2 to compare the config files''')
a = int(input())
if (a==1):
    url_service_function()
elif(a==2):
    url_service_function1()
else:
    print("Wrong choice")

