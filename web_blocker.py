import time
from datetime import datetime as dt

host_temp= "hosts" #this is the testing path, we copied the hosts path from root/C to here to test the script.
host_path = "/etc/hosts" #for windows the host_path is "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
"""example of webpages you want to block"""
web_list=["www.facebook.com","facebook.com","Yahoo.com","123movieshub.com","https://123movieshub.com/"]



while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,19) < dt.now() < dt(dt.now().year,
    dt.now().month, dt.now().day,21,49):       #19 and 21,49 specify the time from when to when you want to block the pages
        print("websites cannot be launched")

        with open(host_path, 'r+') as file:    #working hours
            content = file.read()
            for website in web_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:           #out of working hours
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
            file.truncate()
        print("websites free to be launched")
    time.sleep(4)
    #note you should execute the script as root/admin
