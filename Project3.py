import re
from datetime import datetime

now = datetime.now()
dataToSend = "\nDate:" + str(now) + "\n\n"
data = {}

with open(r"C:\Shared\access.log", "r") as logFile:
    for line in logFile:
        errorCapt = re.search(r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*(\[.*?\]).*\s(404)\s", line)
        if errorCapt:
            ip = errorCapt.group(1)
            #print(ip)
            dateTime = errorCapt.group(2)
            #print(dateTime)
            error = errorCapt.group(3)
            #print(error)

            dataToSend += dateTime +" \tIP: " + ip + " \t Error:" + error + "\n"

 
#print (dataToSend)

with open(r"C:\Shared\error_Findings.txt", "w") as toFile:
    toFile.write(dataToSend)