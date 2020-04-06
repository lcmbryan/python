########################################################
##  Author      : Bryan Leong
##  Date        : 22 July 2019
##  Version     : 0.1
##  Description : Draft version of dashboard_auto. This program is automatic desktop application open and login to different website by itself.
########################################################
import os
import platform
import config
import socket
import subprocess
import sys
import time


def clear_screen():

    if platform.system()=='Windows':
        os.system("cls")
    if platform.system()=='Linux':
        os.system("clear")

def menu():
    hostInfo()
    while True:
        try:
            print("--------------------")
            print("QA Utility")
            print("--------------------")
            print("1. Installation")
            print("2. Smoke Test")
            print("3. Regression Test")
            print("4. Start RADIUS server")
            print("5. Start/Stop Nagios Server")
            print("6. Backup")
            print("7. Execute CIS daily script")
            print("0. Quit")
            choice = int(input("Enter your choice: "))
            clear_screen()

            if choice == 1:
                print("You choose to install new SAA")
            if choice == 2:
                print("You choose to run smoke test")
            if choice == 3:
                print("You choose to regression test")  
            if choice == 0:
                print("Bye")
                break
                exit
        except ValueError:
                clear_screen()
                print("You put in invalid option. Try again")

def hostInfo():
    print("-------- SYSTEM INFO --------")
    host_name = socket.gethostname() 
    host_ip = socket.gethostbyname(host_name) 
    home_dir = os.path.expanduser("~")
    #user_name = os.getlogin()
    #print("Username: "+user_name)
    print("Home Dir: "+home_dir)
    print("Hostname: "+host_name)
    print("IP Addr: "+host_ip)

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    count = 1
    listOfFile = os.listdir(dirName)
    allFiles = list()

    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        print(str(count) +". " + entry)
        count = count + 1
    print("0. Back to Main menu")

    while True:
        choice = int(input("Enter your choice: "))
        if choice > count:
            print("Wrong selection.")
            continue
        print("Selection: "+listOfFile[choice])
        if choice == 0:
            clear_screen()
            menu()
        break
    #     fullPath = os.path.join(dirName, entry)
    #     # If entry is a directory then get the list of files in this directory 
    #     if os.path.isdir(fullPath):
    #         allFiles = allFiles + getListOfFiles(fullPath)
    #     else:
    #         allFiles.append(fullPath)
                
    # return allFiles

# Create the file if not exist and write the data into it.
def writeToFile(filePath):
    file=filePath
    with open(file, 'a+') as f:
        data = 'some data to be written to the file'
        f.write(data+'\n')

def readFromFile(filePath):
    file=filePath
    with open(file, 'r') as f:
        data = f.read()

def mapShareDrive():
    print("Mapping drive Q to PAC_Share")
    os.system("net use q: \\\\bewxp042\PAC_Share")
    # To show current map drive os.system("net use")

def startRadiusServer():
    os.system('P:\Internal_Tools\RadiusServer\new\.\rad-SAG.bat')

def remoteControl():
    HOST="www.example.org"
    # Ports are handled in ~/.ssh/config since we use OpenSSH
    COMMAND="uname -a"

    ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print(result)

    # os.system('ssh username@ip  bash < local_script.sh >> /local/path/output.txt 2>&1')
    # os.system('ssh username@ip  python < local_program.py >> /local/path/output.txt 2>&1')

def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for line in process.stdout:
        print(line)
        result.append(line)
    errcode = process.returncode
    # for line in result:
    #     print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)

##### Reference #####

# do the client machines have python loaded? if so, I'm doing this with psexec
# On my local machine, I use subprocess in my .py file to call a command line.

# import subprocess
# subprocess.call("psexec {server} -c {}") 

# the -c copies the file to the server so i can run any executable file (which in your case could be a .bat full of connection tests or your .py file from above).

###########################

run_win_cmd("C:\\Temp\\test.bat&dir")

############## MAIN ROUTINE ##############

    # HOST="localhost"
    # # Ports are handled in ~/.ssh/config since we use OpenSSH
    # COMMAND="uname -a"

    # ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
    #                     shell=True,
    #                     stdout=subprocess.PIPE,
    #                     stderr=subprocess.PIPE)
    # result = ssh.stdout.readlines()
    # if result == []:
    #     error = ssh.stderr.readlines()
    #     print >>sys.stderr, "ERROR: %s" % error
    # else:
    #     print(result)
# subprocess.Popen('C:&cd Temp&test.bat', shell=True)

# from subprocess import Popen, PIPE
# process = Popen( "cmd.exe", shell=False, universal_newlines=True,
#                   stdin=PIPE, stdout=PIPE, stderr=PIPE )                             
# out, err = process.communicate( commands ) 

#getListOfFiles('C:\Temp')
#menu()
# mapShareDrive()
#os.system('C:\PROGRA~1\PuTTY\plink.exe sdglogin@192.168.5.214 ls -ltr /tmp; hostname; uname')
# os.system('P:\Internal_Tools\RadiusServer\new\.\rad-SAG.bat')

#writeToFile('C:\Temp\Test.txt')
#directory=os.listdir('C:\\Temp')
# print(directory)
# listOfFiles = getListOfFiles('C:\Temp')

#     # Print the files
# for elem in listOfFiles:
#     print(elem)

# listOfFiles = getListOfFiles('C:\Temp')
# print(listOfiles)


################ Cosmetic effect ##################
# while True:
#     clear_screen()
#     print("Welcome to QA Utility")
#     time.sleep(3)
#     clear_screen()
#     print("Loading...")
#     time.sleep(2)
#     clear_screen()
#     menu()
#     break
###################################################

