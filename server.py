import socket
from monster import Monster
from _thread import *
import threading
import pickle
from time import *

HOST = 'localhost'
PORT = 5555

print('Starting Server...')

# Socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding
try:
    s.bind((HOST, PORT))
except socket.error as e:
    str(e)

# Waiting for 2 players
s.listen(2)
print(f'Listening for connections on port {PORT}')

while True:
    p1Connection, p1Address = s.accept()
    if p1Connection:
        print(f'Player 1 connected form port {p1Address}')
        break

while True:
    p2Connection, p2Address = s.accept()
    if p2Address != p1Address:
        print(f'Player 1 connected form port {p2Address}')
        break

print('Both players are connected')
sleep(1)
print('Waiting for players to ready up...')
s.setblocking(False)

while True:

    try:
        p1_data = p1Connection.recv(2048)
        print(f'Player 1 {p1_data}')
    except socket.error as e:
        print(e)

    try:
        p2_data = p2Connection.recv(2048)
        print(f'Player 2 {p2_data}')
    except socket.error as e:
        print(e)

    p2Connection.send(str(p1_data).encode('utf-8'))
    p1Connection.send(str(p2_data).encode('utf-8'))
    print('Sending start to both players')

    break

turn = 1
round = 1

while True:

    # Receive command
    try:
        p1_data = p1Connection.recv(2048).decode('utf-8')
    except:
        pass

    try:
        p2_data = p2Connection.recv(2048).decode('utf-8')
    except:
        pass

    p2Connection.send(str(p1_data).encode('utf-8'))
    p1Connection.send(str(p2_data).encode('utf-8'))


p1Connection.close()
p2Connection.close()

print('Closed sockets')


