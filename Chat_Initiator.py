from Peer_Discovery import clients
import socket
import json

chatInitiator = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(clients)

# client = input("Who do you want to message? ")
# if client not in clients:
#     print(f"{client} does not exist")
# addr = clients[client]

username = input("whats your username: ")

def secureConnection():
    secure_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_socket.connect(addr)
    p = 23
    g = 5
    secretKey = 4
    temp = (g^secretKey)%p
    secure_socket.send(str(temp).encode())
    temp2 = int(secure_socket.recv(1024).decode())
    finalKey = (temp2^secretKey)%p
    print(finalKey)
    secure_socket.close()


addr = ('192.168.1.60',6001)
chatInitiator.connect(addr)

print("connected")
connectionMode = input("do you want an encrypted or unencrypted chat? ")
if connectionMode == "encrypted":
    message = (f"encrypted chat request from {username}")
    chatInitiator.send(message.encode())
    secureConnection()
else:
    message = (f"chat request from {username}")
    chatInitiator.send(message.encode())



chatInitiator.close()
