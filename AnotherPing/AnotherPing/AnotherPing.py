
#s = socket(AF_INET, SOCK_STREAM)         # Creates socket
#host = 'localhost' # Enter the IP of the workstation here 
#port = 80                # Select port which should be pinged

#try:
#    s.connect((host, port))    # tries to connect to the host
#except ConnectionRefusedError: # if failed to connect
#    print("Server offline")    # server is offline

#s.close()                      # close socket


#====================================================
#This is a working code
import subprocess

hostname = "172.16.0.1"
output = subprocess.Popen(["ping.exe",hostname],stdout = subprocess.PIPE).communicate()[0]

print(output)

#Code below causing Type str doesn't support the buffer API

#if ('unreachable' in output):
#    print("Offline")



#=============================================================
#import time
#import random
#import select
#import socket
 
 
#def chk(data):
#    x = sum(a + b * 256 for a, b in zip(data[::2], data[1::2] + b'\x00')) & 0xFFFFFFFF
#    x = (x >> 16) + (x & 0xFFFF)
#    x = (x >> 16) + (x & 0xFFFF)
#    return (~x & 0xFFFF).to_bytes(2, 'little')
 
 
#def ping(addr, timeout=1):
#    with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as conn:
#        payload = random.randrange(0, 65536).to_bytes(2, 'big') + b'\x01\x00'
#        packet  = b'\x08\x00' + b'\x00\x00' + payload
#        packet  = b'\x08\x00' + chk(packet) + payload
#        conn.connect((addr, 80))
#        conn.sendall(packet)
 
#        start = time.time()
 
#        while select.select([conn], [], [], max(0, start + timeout - time.time()))[0]:
#            packet    = conn.recv(1024)[20:]
#            unchecked = packet[:2] + b'\0\0' + packet[4:]
 
#            if packet == b'\0\0' + chk(unchecked) + payload:
#                return time.time() - start
 
 
#if __name__ == '__main__':
#    print(ping('google.com'))