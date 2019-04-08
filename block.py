import time
from datetime import datetime as dt

path = r"C:\Users\hp\PROJECTZ!!\Web blocker\hosts"  #test path
original = r"C:\Windows\System32\drivers\etc\hosts"  # original destination to work with this code
redirect = "127.0.0.1"
website = ["www.facebook.com", "facebook.com", "www.netflix.com", "netflix.com",         
           "primevideo.com", "www.primevideo.com", "youtube.com", "www.youtube.com"]     # sites you want to block from access 
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,9):    # time for which you want them to be blocked
        print("Time to work!!")
        with open(original, "r+") as file:                # <---- Original Path passed as the hosts filw of Windows
            filetext = file.read()
            for site in website:
                if site in filetext:                               
                    pass                                       # if the sites you provided are already in a file it will do nothing
                else:
                    file.write("\n"+ redirect +" "+site+"\n")  # if not present it will add these sites to your host

    else:
        with open(original, 'r+') as file:                  #  # <---- Original Path passed as the hosts file of Windows 
            filetext = file.readlines()                     
            file.seek(0)                                      # brings the pointer to the start
            for line in filetext:
                if not any(site in line for site in website):  
                    file.write(line)
            file.truncate()                            # truncate deletes the file content from cupprent point to downward      # here comes the tricky part 
        print("Do anything!!")
    time.sleep(5)

'''the trick that is pulled here is that, when you have those sites added to your hosts file now after a certain period of time you have to remove
that sites in order to aceess them later. There is no function or method defined to delete the text, thus what we do here is we read the file and check
that if the site names are present in the file, then we write the contents of the file again and then we seek the pointer to the start of the file and we use truncate
to delete the text from file so that we get the original host file back'''

    
