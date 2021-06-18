"""import socket
import threading as th
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverip=input("Enter Server IP : ")
print()
#serverip="192.168.0.109"
serverport=1234


port=4444;
ip="192.168.0.108";
s.bind((ip,port));


def rec():
    while True:
        print("Messge form server")
        y=s.recvfrom(1024);   # Receive all info
        client_ip=y[1][0]
        data=y[0].decode();
        print(client_ip + " : "+ data)
        print()

def send():
    while True:
        data=input("Enter msg : ")
        s.sendto(data.encode(),(serverip,serverport))


th.Thread(target=send).start()
th.Thread(target=rec).start()
"""

#    if "bye" in data:
#        break

    
import threading as th
import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

width = os.get_terminal_size().columns                #get terminal size and center the content using this function.

receiverport = 1234                                          #port of the server were this app running
senderport = 4321                                           #port of your server were this app runnigg

print("Welcome to Groovy! Chat Application!".center(width))

senderip = input("\nEnter your IP : ")                      #ip address of this server

receiverip = input("\nEnter your Friends IP : ")              #ip address of receiver server

s.bind((senderip,senderport))

def sender():
       while True:
            sndmsg = input("\n")
            s.sendto(bytes(sndmsg.encode()),(receiverip,receiverport))
            if "bye" in sndmsg  or "see you soon" in sndmsg:
                 exit()

def receiver():
       while True:
            rcvmsg = s.recvfrom(1024)
            data = rcvmsg[0].decode()
            msg="Message From "+ rcvmsg[1][0]+ " : "+data
            print(msg.center(100))
            if "bye" in data or "see you soon" in data:
                 exit()

th.Thread(target=sender).start()
th.Thread(target=receiver).start()
    