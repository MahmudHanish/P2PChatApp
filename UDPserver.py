import socket
import json
import time

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket options to allow multiple sockets to bind to the same port
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the server address and port
server_address = ('192.168.1.33', 6000)
server_socket.bind(server_address)

# Dictionary to store peer IDs and last seen timestamps
peer_dict = {}

clients = {}

print("Server is listening on", server_address)

# def display_available_users(peer_dict):
#     current_time = time.time()
#     print("Available users:")
#     for peer_id, last_seen in peer_dict.items():
#         if current_time - last_seen <= 900:
#             status = "(Online)"
#         elif current_time - last_seen <= 10:
#             status = "(Away)"
#         else:
#             continue
#         print(f"{peer_id} {status}")
def display_available_users(peer_dict):
    current_time = time.time()
    available_users = "Available users:\n"
    for peer_id, last_seen in peer_dict.items():
        if current_time - last_seen <= 10:
            status = "(Online)"
        elif current_time - last_seen > 10:
            status = "(Away)"
        else:
            continue
        available_users += f"{peer_id} {status}\n"
    return available_users

while True:
    # Receive message from client
    data, client_address = server_socket.recvfrom(1024)

    # Add client to the list if not already present
    if client_address not in clients.values():
        clients[data] = client_address
    
    
    try:
        # Parse JSON data
        json_data = json.loads(data.decode())
        peer_id = json_data['id']
        # Update peer dictionary with current timestamp
        peer_dict[peer_id] = time.time()	
    except json.JSONDecodeError:
        print("Invalid JSON format received")
    

    for name, addr in clients.items():
        if addr != client_address:
            server_socket.sendto(str(display_available_users(peer_dict)).encode(), addr)
    

    time.sleep(8)  # Adjust as needed for periodic announcements


