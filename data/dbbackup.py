#https://www.techbeamers.com/python-copy-file/
import os
from datetime import datetime

Filepath = '.\\dane.txt'
#Get last modification time of a file using os.path.getmtime()
modifiedTime = os.path.getmtime(Filepath)

timestamp = datetime.fromtimestamp(modifiedTime).strftime("%b-%d-%Y_%H.%M.%S")

#prevName = '.\\dane.txt'
#newName = 'backup\\dane.txt'

os.popen('copy dane.txt backup\\dane_{}.txt'.format(timestamp))
#os.rename(prevName,newName+"_"+timestamp + ".txt")
print("Last modifiedTime: ",timestamp)

now = datetime.now()
current_time = now.strftime("%Y/%m/%d, %H:%M:%S")
#os.popen('copy dane.txt backup\\dane_{}.txt'.format(current_time))
print("Current time: ",current_time)
