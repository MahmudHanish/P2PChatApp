import socket
import json
import time

# Create a UDP socket for server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket options to allow multiple sockets to bind to the same port
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
# Bind the UDP socket to the server address and port
server_address = ('192.168.1.33', 6000)
server_socket.bind(server_address)

# Create a TCP socket for chat requests
chatRequestSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chatRequestSocket.bind(('192.168.1.33', 6001))
chatRequestSocket.listen(1)

# Dictionary to store client information (indexed by username and IP address)
clients = {}

print("Server is listening on", server_address)

def usernameSender(client_address):
    connectionSocket, client_address = chatRequestSocket.accept()
    chatRequest = connectionSocket.recv(1024).decode()
    
    if chatRequest == "1":
        connectionSocket.send("Searching for users...".encode())        
    else:
        connectionSocket.send(str(clients.get(chatRequest)).encode())
    connectionSocket.close()


def display_available_users(clients):
    current_time = time.time()
    available_users = "Available users:\n"
    for (username, ip), client_info in clients.items():
        last_seen = client_info[1]  # Get the last seen timestamp from the client info tuple
        if current_time - last_seen <= 10:
            status = "(Online)"
        elif current_time - last_seen >= 900:
            status = "(Away)"
        else:
            continue
        available_users += f"{username} from {ip} {status}\n"
    return available_users

while True:
    # Receive message from client
    data, client_address = server_socket.recvfrom(1024)

    # Accept incoming chat requests

    try:
        # Parse JSON data
        json_data = json.loads(data.decode())
        username = json_data.get('username')
        if username:
            # Store client information along with the current timestamp
            clients[(username, client_address[0])] = (client_address, time.time())
    except json.JSONDecodeError:
        print("Invalid JSON format received")
    
    # Send the list of available users to the client
    server_socket.sendto(display_available_users(clients).encode(), client_address)

    # Process the chat request
    print('1st done')
    usernameSender(client_address)
    print('funk')
    time.sleep(8)  # Adjust as needed for periodic announcements
