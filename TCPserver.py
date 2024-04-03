from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')



while 1:
	connectionSocket, addr = serverSocket.accept()
	temp1 = connectionSocket.recv(1024)
	x = temp1.decode()
	temp2 = connectionSocket.recv(1024)
	y = temp2.decode()
	temp3 = connectionSocket.recv(1024)
	z = temp3.decode()

	print(x,y,z)

	if z == 1 :
		calculation = int(x)+int(y)
	else:
		calculation = int(x)-int(y)
		
	print(calculation)
	connectionSocket.send(calculation.encode())
	connectionSocket.close()