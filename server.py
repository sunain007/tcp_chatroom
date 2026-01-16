import socket
import threading

import os

if not os.path.exists("bans.txt"):
    open("bans.txt", "w").close()

host = '192.168.1.64'   # replace it with your local IP address
port =  5553
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients[:]:
        try:
            client.send(message)
        except:
            clients.remove(client)
            client.close()


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            msg = message.decode('ascii')

            index = clients.index(client)
            nickname = nicknames[index]

            if msg.startswith('KICK'):
                if nickname == 'admin':
                    name_to_kick = msg.split(' ', 1)[1]
                    kick_user(name_to_kick)
                else:
                    client.send("Command refused!".encode('ascii'))

            elif msg.startswith('BAN'):
                if nickname == 'admin':
                    name_to_ban = msg.split(' ', 1)[1]
                    kick_user(name_to_ban)
                    with open('bans.txt', 'a') as f:
                        f.write(name_to_ban + "\n")
                else:
                    client.send("Command refused!".encode('ascii'))

            else:
                broadcast(message)

        except:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f"{nickname} left the chat".encode('ascii'))
                nicknames.remove(nickname)
                break

def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii')) 
        nickname = client.recv(1024).decode('ascii') 

        with open('bans.txt', 'r') as f:
            bans = f.readlines()
        if nickname+'\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        if nickname == 'admin':
            client.send('PASS'.encode('ascii'))
            password=client.recv(1024).decode('ascii')
            if password != 'adminpass':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue
             
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} joined the chat !!!'.encode('ascii'))
        client.send('Connected to the server !!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()  

def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]
        clients.remove(client_to_kick)
        client_to_kick.send('You were kicked by admin!!'.encode('ascii'))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} was kicked by admin!!'.encode('ascii'))


print("Server is running...") 
receive()