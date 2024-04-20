import socket
import json
import time

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('192.168.1.33', 6000)

# Client ID
client_id = input("Enter your ID: ")


# Call this function to display available users
while True:
    # Create JSON message
    message = json.dumps({'id': client_id})
    
    # Send periodic announcements to the server
    client_socket.sendto(message.encode(), server_address)
    
    users = client_socket.recv(1024)

    print(users.decode())
    # Wait for a while before sending the next announcement
    time.sleep(8)  # Adjust as needed for periodic announcements

