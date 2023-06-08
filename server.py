import socket 

def showmessage(message):
    print(f"client: {message}")

print("Server")
print("Digite localhost para teste local ou o ip do servidor:")
host = input()

print("Digite a porta do servidor:")
port = int(input())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

clientsocket, adr = s.accept()

print(f"Server running on {socket.gethostname()}:8000")

while True:
    msg = clientsocket.recv(1024)
    if(msg):
        showmessage(msg.decode("utf-8"))

socket.close()