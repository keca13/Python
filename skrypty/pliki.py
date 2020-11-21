#!/usr/bin/python3
import time, os, sys

path_from = sys.argv[1]

def readFromFile(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'r')
            server_config = server_file.read()
        print(server_config)
        server_file.close()

def writeToFile(*path_to_files):
    if path_to_files is not None:
        for path in path_to_files:
            server_file = open(path, 'w')
            title = "DEVELOPER MODE\n"
            server_file.write(title)
            # server_params = ['CPU=20\n', 'RAM=300\n', "TOTALDISK=3\n", "\tD:\\, C:\\\n"]
            server_params = [ "CPU=20\n", "RAM=300G\n", "TOTALDISK=3\n", "\t/dev/sda, /dev/sdb\n" ]
            server_file.write(''.join(server_params))
        server_file.close()

start_time = time.localtime()
print("Script start time: {} {} {} ".format(start_time.tm_hour, start_time.tm_min, start_time.tm_sec))

stage = os.getenv("STAGE", default='dev').upper()

if stage.startswith('PROD'):
    output = f"SERVER is in {stage} mode"
    print(output)
    exit()
elif os.path.exists(path_from):#kiedy plik istnieje
    readFromFile(path_from)
else:
    writeToFile(path_from)#kiedy plik nie istnieje

stop_time = time.localtime()
diffrence = time.mktime(stop_time) - time.mktime(start_time)
print("Script stopped at: {}".format(time.strftime("%X", stop_time)))
print("Total time {} seconds".format(diffrence))