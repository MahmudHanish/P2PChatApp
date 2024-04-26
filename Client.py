import socket
import json
import time


# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Create a TCP socket for initiation
initiationSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Server address and port
serverUDPaddress = ('192.168.1.33', 6000)
serverTCPaddress = ('192.168.1.33', 6001)
groveries= ['apples','bannnnas']

# Client ID
client_id = input("Enter your ID: ")

# Call this function to display available users
username = json.dumps({'username': client_id})

def getUserIP():
    initiationSocket.connect(serverTCPaddress)
    connect = input("Who do you want to connect with? (press 1 to continue searching): ")

    if connect == "1":  # Compare with string "1"
        print(initiationSocket.recv(1024).decode())
    else:
        initiationSocket.send(connect.encode())
        requestedUser = initiationSocket.recv(1024).decode()
        print(requestedUser)
    initiationSocket.close()
    

while True:
    # Send periodic announcements to the server
    print("connecting to server")
    client_socket.sendto(username.encode(), serverUDPaddress)
    print("username sent")

    users = client_socket.recv(1024)
    
    print(users.decode())

    getUserIP()
    
    # Wait for a while before sending the next announcement
    time.sleep(8)  # Adjust as needed for periodic announcements


