import time
from datetime import datetime as dt

host_temp= "hosts" """the testing location of hosts for windows, for testing the script"""
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"  """the real location path of hosts for windows"""
redirect = "127.0.0.1"
"""example of webpages you want to block"""
web_list=["www.facebook.com","facebook.com","Yahoo.com","123movieshub.com","https://123movieshub.com/"]



while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,18) < dt.now() < dt(dt.now().year,
    dt.now().month, dt.now().day,21,49):      """The time of blocking websites, my example from 18:21, can be changed to whatever time you want """
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
