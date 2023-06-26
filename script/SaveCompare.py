import subprocess
import re
import time
import argparse

def copy_osconfig(release_name):
    # Using readlines()
    file1 = open('conf/configuration_os.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #rel_name = input("Enter the release name\n")
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

        subprocess.check_output("mkdir -p $PWD/.siddos/"+ release_name +"", shell=True)
        subprocess.run(""+ command +" 2>/dev/null >> $PWD/.siddos/"+ release_name +"/"+file+"", shell=True)


def copy_appconfig(release_name):
    # Using readlines()
    file1 = open('conf/configuration_app.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #rel_name = input("Enter the release name\n")
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

        subprocess.check_output("mkdir -p $PWD/.siddapp/"+ release_name +"", shell=True)
        subprocess.run(""+ command +" 2>/dev/null >> $PWD/.siddapp/"+ release_name +"/"+file+"", shell=True)


def stop_service():
    subprocess.call("service apache2 stop", shell=True)
    subprocess.call("service apache2 status", shell=True)
    main_func()

def deploy_service():
    file1 = open('conf/configuration.txt', 'r')
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

def compare_osconfig(release1, release2):
    x = subprocess.check_output("cat conf/configuration_os.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > conf/configuration1_os.txt", shell=True)
    
    # Using readlines()
    file1 = open('conf/configuration1_os.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #Strips the newline character

    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())

        s1 = re.compile(r'[,][a-zA-Z_.]+')
        m1 = s1.search(a1)
        file=m1.group().lstrip(',')

        print("******Works start**********")
        print("Showing the difference between $PWD/.siddos/"+ release2 +"/"+ file +"  and $PWD/.siddos/"+ release1 +"/"+ file +"")
        subprocess.call("diff $PWD/.siddos/"+ release2 +"/"+ file +" $PWD/.siddos/"+ release1 +"/"+ file +"", shell=True)
        subprocess.check_output("rm -rf conf/configuration1_os.txt", shell=True)
        print("******Done*********")
        #time.sleep(3)

    print("********Completed the Work***********")

def compare_appconfig(release1, release2):
    x = subprocess.check_output("cat conf/configuration_app.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > conf/configuration1_app.txt", shell=True)

    # Using readlines()
    file1 = open('conf/configuration1_app.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #Strips the newline character

    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())

        s1 = re.compile(r'[,][a-zA-Z_.1-9]+')
        m1 = s1.search(a1)
        file=m1.group().lstrip(',')

        print("******Works start**********")
        print("Showing the difference between /home/siddapp/"+ release2 +"/"+ file +"  and /home/siddapp/"+ release1 +"/"+ file +"")
        subprocess.call("diff $PWD/.siddapp/"+ release2 +"/"+ file +" $PWD/.siddapp/"+ release1 +"/"+ file +"", shell=True)
        subprocess.check_output("rm -rf conf/configuration1_app.txt", shell=True)
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

def connectivity_test(test_type):

    def test_code():
        pass_count = 0
        fail_count = 0
        fail_count1 = 0
        fail_count2 = 0
        pass_host = []
        fail_host1 = []
        fail_host2 = []

        print("================================SUMMARY=========================")
        file3 = open('logs/file.txt', 'r')
        Lines = file3.readlines()
        file3.close()

        for line in Lines:
            a1 = "{}".format(line.strip())

            if 'succeeded' in a1:
                pass_count = pass_count + 1

                s1 = re.compile(r'Connection to [A-Za-z_-]+')
                m1 = s1.search(a1)
                temp_host1 = m1.group().lstrip('Connection to ')
                host1 = temp_host1+':'

                s2 = re.compile(r'[0-9]+ port')
                m2 = s2.search(a1)
                port1 = m2.group().rstrip(" port")

                pass_host.append(host1+port1)

            elif 'Name or service not known' in a1:
                fail_count1 = fail_count1 + 1

                s3 = re.compile(r'"[A-Za-z_-]+"')
                m3 = s3.search(a1)
                temp_host2 = m3.group().lstrip('"').rstrip('"')
                host2 = temp_host2+':'

                s4 = re.compile(r'port [0-9]+')
                m4 = s4.search(a1)
                port2 = m4.group(0).lstrip("port ")

                fail_host1.append(host2+port2)

            elif 'No address associated with hostname' in a1:
                fail_count2 = fail_count2 + 1

                s5 = re.compile(r'"[A-Za-z_-]+"')
                m5 = s5.search(a1)
                temp_host3 = m5.group().lstrip('"').rstrip('"')
                host3 = temp_host3+':'

                s6 = re.compile(r'port [0-9]+')
                m6 = s6.search(a1)
                port3 = m6.group(0).lstrip("port ")

                fail_host2.append(host3+port3)

        fail_count = fail_count1 + fail_count2
        print("Total =>",pass_count + fail_count)
        print("----------------------------------------------------------------")
        print("Passed =>",pass_count)
        for i in pass_host:
            print (i)
        print("----------------------------------------------------------------")
        print("Failed =>",fail_count)
        if (fail_count > 0):
            if (fail_count1 > 0):
                print("\nReason => Name or service not known")
                for i in fail_host1:
                    print(i)

            elif (fail_count2 > 0):
                print("\nReason => No address associated with hostname")
                for i in fail_host2:
                    print(i)
        print("----------------------------------------------------------------")
        print("================================END=========================")


    def url_service_function():
        x = subprocess.check_output("cat conf/configuration_url_service.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > conf/configuration.txt", shell=True)
    
        # Using readlines()
        file1 = open('conf/configuration.txt', 'r')
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
    
        subprocess.check_output("rm -rf conf/configuration.txt", shell=True)
        print("********************Completed****************")
    
    def manual_change_function():
        x1 = subprocess.check_output("cat conf/configuration_manual_change.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > conf/configuration1.txt", shell=True)
        x2 = subprocess.call("rm -rf logs/file.txt", shell=True)
        
        # Using readlines()
        file2 = open('conf/configuration1.txt', 'r')
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
            
            y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"; nc -vz -w 5 "+ host +" "+ port +" >> logs/file.txt 2>&1", shell=True)
    
            print("********************Done****************")
            time.sleep(3)
    
        subprocess.check_output("rm -rf conf/configuration1.txt", shell=True)
        test_code()
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

    if( test_type=='url' ):
        print("*****************Checking the connection starts****************")
        url_service_function()
    elif( test_type=='mc' ):
        manual_change_function()
    elif( test_type=='mi' ):
        manual_input()
    else:
        print("You gave wrong choice, pls give right input")


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', dest='save', help='Save the os/app releated config files', type=str)
    parser.add_argument('-C', dest='config', help='Configuration you would like to save os or app', type=str)
    parser.add_argument('-N', dest='name', help='Name of the release', type=str)
    parser.add_argument('-com', dest='compare', help='Compare', type=str)
    parser.add_argument('-rel1', dest='rel1', help='Release1 Name', type=str)
    parser.add_argument('-rel2', dest='rel2', help='Release2 Name', type=str)
    parser.add_argument('-con', dest='connect', help='connect', type=str)
    parser.add_argument('-type', dest='type', help='Type of connectivity test', type=str)
    args = parser.parse_args()
    
    release_name = args.name
    release1 = args.rel1 
    release2 = args.rel2
    test_type = args.type

    if (args.save=='save' and args.config=='os'):
        copy_osconfig(release_name)
    elif (args.save=='save' and  args.config=='app'):
        copy_appconfig(release_name)
    elif (args.compare=='compare' and args.config=='os'):
        compare_osconfig(release1, release2)
    elif (args.compare=='compare' and args.config=='app'):
        compare_appconfig(release1, release2)
    elif (args.connect=='connect'):
        connectivity_test(test_type)
    else:
        print('''python3 SaveCompare.py -S save -C <os|app> -N name
python3 Savecompare.py -com compare -C <os|app> -rel1 release_name -rel2 release_name
python3 SaveCompare.py -con connect -type <url|mc|mi>''')

