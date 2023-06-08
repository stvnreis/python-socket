import socket

print("Client")
print("Digite localhost para teste local ou o Ip do servidor:")
host = input()

print("Digite a porta do servidor:")
port = int(input())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    message = input()
    
    if(message == "SAIR"):
        s.send(bytes("Encerrando conexão", "utf-8"))
        break
    
    s.send(bytes(message, "utf-8"))
s.close()