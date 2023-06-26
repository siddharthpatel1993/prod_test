#passed - Connection to localhost 80 port [tcp/http] succeeded!
#failed -  nc: getaddrinfo for host "grafana" port 3000: Name or service not known

import re

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

test_code()
