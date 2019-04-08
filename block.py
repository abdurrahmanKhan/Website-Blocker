import time
from datetime import datetime as dt

path = r"C:\Users\hp\PROJECTZ!!\Web blocker\hosts"

original = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website = ["www.facebook.com", "facebook.com", "www.netflix.com", "netflix.com",
           "primevideo.com", "www.primevideo.com", "youtube.com", "www.youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10):
        print("Time to work!!")
        with open(original, "r+") as file:
            filetext = file.read()
            for site in website:
                if site in filetext:
                    pass
                else:
                    file.write("\n"+ redirect +" "+site+"\n")

    else:
        with open(original, 'r+') as file:
            filetext = file.readlines()
            file.seek(0)
            for line in filetext:
                if not any(site in line for site in website):
                    file.write(line)
            file.truncate()
        print("Do anything!!")
    time.sleep(5)
