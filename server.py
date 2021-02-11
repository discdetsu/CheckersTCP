import socket
from game import Player
from monster import Monster
from _thread import *
import threading
import pickle

HOST = 'localhost'
PORT = 5555

# Socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding
try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

# Waiting for 2 players
s.listen(2)
print("Waiting for a connection, Server Started")
players = []


def client_thread(conn):
    conn.send(str.encode('Connected to the server!'))
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')

            if not data:
                print('Disconnected')
                break
            else:
                print(f'Received: {reply}')
                print(f'Sending: {reply}')

            conn.sendall(str.encode(reply))
        except:
            break
    print('Lost connection')
    conn.close()

while True:

    connection, clientAddress = s.accept()
    print(f'Connected by: {clientAddress}')

    # data = connection.recv(2048)
    # monster = pickle.loads(data)

    start_new_thread(client_thread, (connection,))

