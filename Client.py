import socket
client=socket.socket()
client.bind(('localhost',8001))
client.connect(('localhost',3334))
client.send(bytes(input('ENTER UR NAME: '),'UTF-8'))
while True:
        inp=input('                             YOUR WORD: ')
        client.send(bytes(inp,'utf-8'))
        if(inp=="bye"):
                exit()
                break
        word=client.recv(1024).decode()
        print("SERVER:",word)
        if(word=="bye"):
                exit()
                break
def exit():
        server.close()
