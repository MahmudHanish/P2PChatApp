import socket
import time
import json


chatResponder = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('', 6001)  # Use port 6001 for chat
chatResponder.bind(server_address)
chatResponder.listen(1)  # Listen for incoming connections (backlog of 1)

print("Responder is listening for incoming connections...")


while True:
    # Accept incoming connection
    client_socket, client_address = chatResponder.accept()
    returnIP = client_address[0]
    json_payload = json.loads(client_socket.recv(1024).decode())
    if json_payload['key'] == 0:


