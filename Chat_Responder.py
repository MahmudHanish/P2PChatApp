import socket
import time


chatResponder = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('', 6001)  # Use port 6001 for chat
chatResponder.bind(server_address)
chatResponder.listen(1)  # Listen for incoming connections (backlog of 1)

def secureConnection(addr):
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


print("Responder is listening for incoming connections...")

history = {}

def usernameExtractor(string):
    temp = string.split()
    username = temp[-1]
    return username

while True:
    # Accept incoming connection
    client_socket, client_address = chatResponder.accept()
    returnIP = client_address[0]
    # Receive message from client
    message = client_socket.recv(1024).decode()
    if client_address[0] not in history:
        print(f"Received connection from: ", client_address)
        history[client_address[0]] = usernameExtractor(message)
        username = usernameExtractor(message)
    print(f"({time.ctime()}) {username}: ", message)
    # if "encrypted" in message:
    #     secureConnection(client_address)
    # else:
    #     pass

    client_socket.close()
    return_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return_address = (returnIP , 6001)
    return_socket.connect(return_address)
    # Optionally, process the message and send a reply
    reply = input("me: ")
    return_socket.send(reply.encode())
    
    # Close the client socket
    return_socket.close()
