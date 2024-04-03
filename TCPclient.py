from socket import *

serverName = '10.0.20.185'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

x = input('Input x: ')
clientSocket.send(x.encode())
y = input('input y: ')
clientSocket.send(y.encode())
z = input('press 1 for addition, press 2 for sub: ')
clientSocket.send(z.encode()) 

calculation = clientSocket.recv(1024)
print(calculation.decode())
clientSocket.close()