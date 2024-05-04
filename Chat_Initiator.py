from Peer_Discovery import getClients
import socket
import time
import json

chatInitiator = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = getClients()
print(clients)

client = input("Who do you want to message? ")
if client not in clients:
    print(f"{client} does not exist")
addr = clients[client]

chatInitiator.connect(addr, 6001)

print(f"connected to {client}")

message = input(": ")

chatInitiator.send(message.encode())

chatInitiator.close()