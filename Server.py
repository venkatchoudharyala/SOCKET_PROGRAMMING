import socket
import time

server=socket.socket()
server.bind(('localhost',3334))
server.listen(5)
print('....SERVER IS READY TO PAIR....')
while True:
        client,addr=server.accept()
        name=client.recv(1024).decode()
        print('connected to:',addr,name)
        while True:
                word=client.recv(1024).decode()
                print(name,':',word)
                if(word=="bye"):
                        exit()
                        break
                inp=input('                             YOUR WORD: ')
                client.send(bytes(inp,'utf-8'))
                if(inp=="bye"):
                        exit()
                        break
def exit():
        server.close()
