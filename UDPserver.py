from socket import *
import json

serverPort = 12000

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind( ('', serverPort) )
print("The server is ready to receive")

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print('received {} bytes from {}'.format(len(message), clientAddress))
	print(message.decode())
	modifiedMessage = f"hello {message.decode()}"
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)
