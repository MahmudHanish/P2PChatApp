import socket
import json
import time


# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Server address and port
serverUDPaddress = ('192.168.1.255', 6000)

# Client ID
client_id = input("Enter your ID: ")

# Storeing your username in a json format
username = json.dumps({'username': client_id})


print(f"Welcome {client_id}")
print("connecting to server")

while True:
    # Send periodic announcements to the server
    client_socket.sendto(username.encode(), serverUDPaddress)


    # Wait for a while before sending the next announcement
    time.sleep(8)  # Adjust as needed for periodic announcements