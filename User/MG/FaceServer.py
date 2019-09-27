# from socket import *
#
# serverSock = socket(AF_INET, SOCK_STREAM)
# serverSock.bind(('', 9055))
# f = open('C:\\GiGaChany\\GiGAChany\\User\\MG')
# serverSock.listen(1)
#
# clientSock, addr = serverSock.accept()
#
# print(str(addr), '에서 접속 확인')
import socket
import sys
s = socket.socket()
s.bind(("10.10.20.37",9055))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

while True:
    sc, address = s.accept()
    print(address)

    f = open("C:/GiGaChany/GiGAChany/User/MG/image.jpg",'wb') # Open in binary
    l = sc.recv(1024)

    while (l):
        f.write(l)
        l = sc.recv(1024)

    f.close()
    sc.close()

s.close()

