import socket
import time

chatResponder = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

chatResponder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 6001)  # Use port 6001 for chat
chatResponder.bind(server_address)
chatResponder.listen(1)  # Listen for incoming connections (backlog of 1)

print("Responder is listening for incoming connections...")

while True:
    # Accept incoming connection
    client_socket, client_address = chatResponder.accept()
    print("Received connection from:", client_address)

    # Receive message from client
    message = client_socket.recv(1024).decode()
    print("Received message:", message)

    # Optionally, process the message and send a reply
    # For now, let's just print the received message
    
    # Close the client socket
    client_socket.close()