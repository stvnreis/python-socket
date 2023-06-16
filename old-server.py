import socket 
import os

def showmessage(message):
    print(f"client: {message}")

host = input("Digite o ip do servidor: ")
port = int(input("Digite a porta do servidor: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

clientsocket, adr = s.accept()

os.system('cls')

print(f"Server running on {host}:{port}")

while True:
    msg = clientsocket.recv(1024).decode('utf-8')
    if(msg):
        if(msg == 'Desconectar servidor'):
            print('Desconectando servidor...')
            break
        showmessage(msg)

s.close()