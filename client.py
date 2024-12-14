import socket
import threading

nickname = input("Choose a nickname : ")

host = '192.168.1.10'
port = 5553

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receiving_thread = threading.Thread(target=recieve)
receiving_thread.start()

writing_thread = threading.Thread(target=write)
writing_thread.start()
