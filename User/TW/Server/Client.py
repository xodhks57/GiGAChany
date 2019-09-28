import socket
import sys

s = socket.socket()
s.connect(("10.10.20.253",9077))
f = open ("C:/GIGA/GiGAChany/User/TW/Server/SendImage/image.jpg", "rb")
l = f.read(1024)
while l:
    s.send(l)
    l = f.read(1024)
    print("카운트")


s.close()

