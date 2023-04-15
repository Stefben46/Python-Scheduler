import time
import sys
import subprocess
import os
from string_list_file import StringListFile

minute = 60
keepTime= 0
filename = sys.argv[1]
wait = int(sys.argv[2])
fileList = StringListFile('Schedule.txt')



def run():
    if os.path.isfile(filename):
        process = subprocess.Popen(['python', filename])
        for sublist in list:
            if sublist[0] == filename:
                fileList.update(filename,str(time.time()))
    else:
        print(f"File {filename} not found in current directory")
        print("> ", end="")
        sys.exit()


list = fileList.read()
for sublist in list:
    if (sublist[0] == filename):
        if  (float(sublist[2]) == 0):
            run()
            keepTime = time.time()
        else:
            keepTime = float(sublist[2])



while True:
    while (time.time()-keepTime<=wait):
        time.sleep(min(minute, wait))
    run()
    keepTime = time.time()

