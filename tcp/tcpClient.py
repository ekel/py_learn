#coding:utf-8
''''''
from socket import *

HOST = '115.159.95.19'
PORT = 21000
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)#.decode()
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()

