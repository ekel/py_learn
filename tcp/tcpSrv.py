'''
from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21566
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write('[%s] %s') % (ctime(), self.rfile.readline().decode().encode())



tcpSrv = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpSrv.serve_forever()
'''
from socket import *
from time import ctime

HOST = ''
PORT = 21000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSvrSock = socket(AF_INET, SOCK_STREAM)
tcpSvrSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcpSvrSock.bind(ADDR)
tcpSvrSock.listen(5)

while True:
    print('waiting for connection...')
    cliSock, addr = tcpSvrSock.accept() #accept会返回两个值
    print('...connected from:', addr)

    while True:
        data = cliSock.recv(BUFSIZ).decode()
        if not data or data == 'exit':
            break
        #cliSock.send(('%s, %s!') % (bytes(ctime(), 'utf-8'),data.decode('utf-8').encode('utf-8')))
        cliSock.send(('[%s] %s' % (ctime(), data)).encode())
    cliSock.close()

tcpSvrSock.close()