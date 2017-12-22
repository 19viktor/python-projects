import time
from datetime import datetime as dt

hostsTemp="hosts"
hostPath=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websiteList=["www.facebook.com","facebook.com","www.youtube.com","youtube.com"]

startTime = 1
endTime = 4

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,startTime) <= dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,endTime):
        with open(hostPath, 'r+') as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + '\n')

    else:
        with open(hostPath, 'r+') as file:
            content = file.readlines()
            #sets pointer to the beginning again
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
    time.sleep(5)
