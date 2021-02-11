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

connection, clientAddress = s.accept()

print(f'Connected by: {clientAddress}')

data = connection.recv(2048)
monster = pickle.loads(data)
connection.close()
print(monster)
