import socket;
import os;
#import time;

#protocol UDP
myp=socket.SOCK_DGRAM;

#net address family :ipv4
afn=socket.AF_INET;

s=socket.socket(afn,myp);

port=1234;
ip="192.168.0.109";

clienip=input("Enter Client IP : ")
print()
#clienip="192.168.0.108"
clientport=4444

s.bind((ip,port));

while(True):
  print("Messge form Client")
  y=s.recvfrom(1024);   # Receive all info
  client_ip=y[1][0]
  data=y[0].decode();
  print(client_ip + " : "+ data)
  print()

  if "bye" in data:
        break

  data=input("Enter msg : ")
  s.sendto(data.encode(),(clienip,clientport))

  
 




