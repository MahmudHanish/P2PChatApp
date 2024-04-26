from socket import *

serverPort = 6001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')



while 1:
	connectionSocket, addr = serverSocket.accept()

	connectionSocket.send()

	received = connectionSocket.recv(2024)

	print(received.decode())


	connectionSocket.close()