"""
import socket;
import os;
import threading as th

#protocol UDP
myp=socket.SOCK_DGRAM;

#net address family :ipv4
afn=socket.AF_INET;

s=socket.socket(afn,myp);

port=1234;
ip="192.168.0.109";

clienip=input("Enter Client IP : ")
#clienip="192.168.0.108"
clientport=4444

s.bind((ip,port));


def rec():
  while True:
    print("Messge form Client")
    y=s.recvfrom(1024);   # Receive all info
    client_ip=y[1][0]
    data=y[0].decode();
    print(client_ip + " : "+ data)


def send():
  while True:
    data=input("Enter msg : ")
    s.sendto(data.encode(),(clienip,clientport))
	
	

th.Thread(target=rec).start()
th.Thread(target=send).start()


#  if "bye" in data:
#        break

  

  
"""





import threading as th
import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

width = os.get_terminal_size().columns #get terminal size and center the content using this function.

receiverport = 1234  #port of the server were this app running
senderport = 4321    #port of your server were this app runnigg
os.system("tput setaf 6")
print("Welcome to Groovy! Chat Application!".center(width))

#os.system("tput setaf 2")

senderip = input("\nEnter your IP : ") #ip address of this server

#os.system("tput setaf 3")
receiverip = input("\nEnter your Friends IP : ") #ip address of receiver server

s.bind((senderip,senderport))

def receiver():
    while True:
        rcvmsg = s.recvfrom(1024)
        data = rcvmsg[0].decode()
        os.system("tput setaf 3")
        msg="Msg from"+ rcvmsg[1][0]+ " : "+data
        print(msg.center(100))
        if "bye" in data or "see you soon" in data:
            exit()

def sender():
    while True:
        sndmsg = input("\n")
        os.system("tput setaf 2")
        s.sendto(bytes(sndmsg.encode()),(receiverip,receiverport))
        if "bye" in sndmsg or "see you soon" in sndmsg:
            exit()

th.Thread(target=receiver).start()
th.Thread(target=sender).start()


