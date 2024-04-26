# from socket import *

# serverName = str(input("enter server ip: "))
# serverPort = 6001
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))



# print("chat initiated")
# message = input("-> ")

# clientSocket.send(message.encode())


# clientSocket.close()

import socket
import threading

# Function to handle incoming messages from the chat partner
def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except ConnectionResetError:
            print("Connection closed by the chat partner.")
            break

# ChatInitiator process
def chat_initiator():
    target_ip = input("Enter the IP address of the user you want to chat with: ")
    target_port = 6000  # Assume a default port for chat

    # Establish connection with the target user
    initiator_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    initiator_socket.connect((target_ip, target_port))

    # Send chat request
    initiator_socket.send("Chat request".encode())

    # Start receiving messages from the chat partner in a separate thread
    receiver_thread = threading.Thread(target=receive_messages, args=(initiator_socket,))
    receiver_thread.start()

    # Send messages to the chat partner
    while True:
        message = input()
        initiator_socket.send(message.encode())

    # Close the socket when the chat ends
    initiator_socket.close()

# ChatResponder process
def chat_responder():
    server_ip = '0.0.0.0'  # Accept connections from any IP address
    server_port = 6000  # Assume a default port for chat

    # Create a socket to listen for incoming chat requests
    responder_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    responder_socket.bind((server_ip, server_port))
    responder_socket.listen(1)

    print("Waiting for chat request...")

    # Accept incoming connection from the initiator
    partner_socket, partner_address = responder_socket.accept()

    # Receive chat request
    request = partner_socket.recv(1024).decode()
    print("Chat request received from", partner_address)

    # Start receiving messages from the chat partner in a separate thread
    receiver_thread = threading.Thread(target=receive_messages, args=(partner_socket,))
    receiver_thread.start()

    # Send messages to the chat partner
    while True:
        message = input()
        partner_socket.send(message.encode())

    # Close the sockets when the chat ends
    partner_socket.close()
    responder_socket.close()

# Main function to start ChatInitiator and ChatResponder processes
def main():
    # Start ChatResponder process in a separate thread
    responder_thread = threading.Thread(target=chat_responder)
    responder_thread.start()

    # Start ChatInitiator process
    chat_initiator()

if __name__ == "__main__":
    main()
