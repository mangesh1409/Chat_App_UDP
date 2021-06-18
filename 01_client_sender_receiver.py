import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverip=input("Enter Server IP : ")
print()
#serverip="192.168.0.109"
serverport=1234

port=4444;
ip="192.168.0.108";
s.bind((ip,port));

while True:
    data=input("Enter msg : ")
    s.sendto(data.encode(),(serverip,serverport))

    if "bye" in data:
        break

    print("Messge form server")
    y=s.recvfrom(1024);   # Receive all info
    client_ip=y[1][0]
    data=y[0].decode();
    print(client_ip + " : "+ data)
    print()

    