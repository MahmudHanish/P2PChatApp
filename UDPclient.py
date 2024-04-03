from socket import *
import json


server_address = ('10.0.20.185', 12000)

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# json meta data
user = '{"username":""}'
temp = json.loads(user)

username = input("whats ur username? ")

temp["username"] = username 

clientSocket.sendto(temp["username"].encode("utf-8"),server_address)

modifiedMessage, server = clientSocket.recvfrom(2048)

print(modifiedMessage.decode("utf-8"))

clientSocket.close()