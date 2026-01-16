import socket
import threading

nickname = input("Choose a nickname : ")
if nickname == 'admin':
    password = input("Enter password for admin: ")

host = '192.168.1.64'    # replace it with you server IP address
port = 5553

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
stop_thread = False

def recieve():
    global stop_thread
    while not stop_thread:
        try:
            message = client.recv(1024)

            if not message:
                print("Disconnected from server")
                stop_thread = True
                break

            msg = message.decode('ascii')

            if msg == 'NICK':
                client.send(nickname.encode('ascii'))

            elif msg == 'PASS':
                client.send(password.encode('ascii'))

            elif msg == 'REFUSE':
                print("Wrong admin password")
                stop_thread = True
                client.close()
                break

            elif msg == 'BAN' or "kicked by admin" in msg.lower():
                print(msg)
                stop_thread = True
                client.close()
                break

            else:
                print(msg)

        except:
            stop_thread = True
            client.close()
            break

def write():
    global stop_thread
    while not stop_thread:
        try:
            msg = input("")
            if stop_thread:
                break

            if msg.startswith('/'):
                if nickname == 'admin':
                    if msg.startswith('/kick '):
                        user = msg.split(' ', 1)[1]
                        client.send(f"KICK {user}".encode('ascii'))
                    elif msg.startswith('/ban '):
                        user = msg.split(' ', 1)[1]
                        client.send(f"BAN {user}".encode('ascii'))
                else:
                    print("Only admin can execute commands")
            else:
                client.send(f"{nickname}: {msg}".encode('ascii'))

        except:
            stop_thread = True
            break



receiving_thread = threading.Thread(target=recieve)
receiving_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()
