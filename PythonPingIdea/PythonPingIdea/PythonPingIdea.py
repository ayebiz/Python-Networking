#Trying to build a workable Python application for IT management
#Objectives 1: input gateway IP (DONE)
#Objectives 2: input remote host IP (DONE)
#Objectives 3: automatically get gateway IP and ping
#Objectives 4: record ping history with timestamp
#Objectives 5: analysis ping result to determine if host is up

#So far this is the only workable lines
#Import os for ping
import os
import sys
#Use sys to avoid input error when entering IP address
sys.stdout.write("Enter IP address: ")
sys.stdout.flush()
ip = sys.stdin.readline()
print("you entered: " + ip)
#Ping the inputed IP address
os.system('ping ' + ip)


#Importable modules are: subprocess; re; shlex; os; sys
#Modules cannot import: wmi
#=====================================
#Get IP address
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#try:
#    s.connect((host, 9))
#    client = s.getsockname()[0]
#except socket.error:
#    client = "Unknown IP"
#finally:
#    del s
#return client
#===================================


#import wmi
#wmi_obj = wmi.WMI()
#wmi_sql = "select IPAddress,DefaultIPGateway from Win32_NetworkAdapterConfiguration where IPEnabled=TRUE"
#wmi_out = wmi_obj.query( wmi_sql )
#for dev in wmi_out:
#    print "IPv4Address:", dev.IPAddress[0], "DefaultIPGateway:", dev.DefaultIPGateway[0]


#===================================
#import subprocess, shlex, re
#strs =  subprocess.check_output(shlex.split('ip r l'))
#match_string = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
#ip = re.search('src '+ match_string, strs).group(1)
#gateway = re.search('default via ' + match_string, strs).group(1)
#print gateway, ip

#========================================
#import subprocess, shlex
#strs = subprocess.check_output(shlex.split('ip r l'))
#gateway = strs.split('default via')[-1].split()[0]
#ip  = strs.split('src')[-1].split()[0]
#print gateway, ip


