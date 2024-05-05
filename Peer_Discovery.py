import socket
import json
import time


server_address = ('', 6000)
# Dictionary to store client information (indexed by username and IP address)

clients = {}

def display_available_users(clients, addr):
    current_time = time.time()
    available_users = "Available users:\n"
    for (username, ip), client_info in clients.items():
        last_seen = client_info[1]  # Get the last seen timestamp from the client info tuple
        if current_time - last_seen < 10:
            status = "(Online)"
        elif current_time - last_seen >= 10:
            status = "(Away)"
        elif current_time - last_seen >= 900:
            status = "(Offline)"
        available_users += f"{username} {status}\n"
    print(available_users)

def peerDiscovery():
    print("Server is listening on", server_address)
    # Create a UDP socket for server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set socket options to allow multiple sockets to bind to the same port
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Bind the UDP socket to the server address and port
    server_socket.bind(server_address)
    while True:
        # Receive message from client
        data, client_address = server_socket.recvfrom(1024)

        # Parse JSON data
        json_data = json.loads(data.decode())
        username = json_data.get('username')
        # Store client information along with the current timestamp
        clients[(username, client_address[0])] = (client_address, time.time())
        # Send the list of available users to the client
        display_available_users(clients, client_address)
        time.sleep(8)  # Adjust as needed for periodic announcements

    

if __name__=="__main__":
    peerDiscovery()

