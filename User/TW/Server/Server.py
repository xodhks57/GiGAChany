import socket
import sys
s = socket.socket()
s.bind(("localhost",9078))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

while True:
    sc, address = s.accept()
    print(address)

    f = open("C:/GIGA/GiGAChany/User/TW/Server/RecvImage/image.jpg",'wb') # Open in binary
    l = sc.recv(1024)

    while (l):
        f.write(l)
        l = sc.recv(1024)

    f.close()
    sc.close()

s.close()




