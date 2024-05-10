import socket
import json
import time


chatInitiator = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

username = input("whats your username: ")

with open('username.json', 'r') as file:
    user = json.load(file)
    username = user['username']

def display_available_users():
    global data
    file_path = 'data.json'
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    current_time = time.time()
    available_users = "Available users:\n"
    for username, client_info in data.items():
        last_seen = client_info[1]  # Get the last seen timestamp from the client info tuple
        if current_time - last_seen < 10:
            status = "(Online)"
        elif current_time - last_seen >= 10:
            status = "(Away)"
        elif current_time - last_seen >= 900:
            del data[username]
        available_users += f"{username} {status}\n"
    print(available_users)

def deffie_hellman():
        secretKey = int(input("choose your secret key: "))
        key = (5^secretKey)%23

def chat():
    client_ID = input("who do you want to chat with? ")
    addr = (data[client_ID],6001)
    chatInitiator.connect(addr)
    secure = input("1 for encrypted chat, 2 for unencrypted chat: ")
    if secure == '1':
        secretKey = int(input("choose your secret key: "))
        key = (5^secretKey)%23
        message = input(f'message: ')
        encrypted_message = message
    if secure == '2':
        message = input("message: ")
        key = 0
        unencrypted_message = message
    json_payload = {"user": username,
                    "key": key,
                    "unencrypted message": unencrypted_message,
                    "encrypted message": encrypted_message
                    }
    chatInitiator.send(json.dumps(json_payload).encode())
    


def mainMenu():
    print("1. Users")
    print("2. Chat")
    print("3. History")
    nav = input("what do you want to do? (use the numbers): ")
    if nav == '1':
        display_available_users()
    elif nav == '2':
        chat()
    elif nav == '3':
        # implement history viewing function here that goes through a folder named logs, each log will be named a previous client
        pass 
    


chatInitiator.close()