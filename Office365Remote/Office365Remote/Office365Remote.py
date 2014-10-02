#Objective1: Run Powershell
#Objective2: Connect to Office 365 remotely
#Objective3: Create Shared mailbox
#Objective4: Create User
#Objective5: Create mailbox

import subprocess
import os
#subprocess.call(["C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe", ".\"./GetCredential.ps1\";", "&hello"])
#subprocess.call(["C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"])
#from subprocess import check_output
#check_output("dir", shell=True)
#os.system('cd /Windows')
#os.system('powershell.exe') #This one works but in home directory
subprocess.call("powershell.exe") #This one also work but in home directory
os.system(".\GetCredential.ps1")
