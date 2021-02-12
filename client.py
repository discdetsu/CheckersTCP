import socket
from monster import Monster
import pickle
import tkinter as tk
from tkinter import *

print('!!!!   Monster Fight  !!!!')

HOST = '158.108.213.72'
PORT = 5555
FORMAT = 'utf-8'

# Create socket object
# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((HOST, PORT))
print('Connected to server')
print('Create monster!')
# data = s.recv(2048).decode(FORMAT)
# print(data)


# Create monster object
name = input('''Please enter your monster's name: ''')
hp = int(input('Health point: '))
atk = int(input('Attack damage: '))
deff = int(input('Defense point: '))
monster = Monster(name, hp, atk, deff)

# Send monster object
dumped_monster = pickle.dumps(monster)
s.send(dumped_monster)
print('sending ready to server')
enemy_ready_message = s.recv(2048).decode(FORMAT)
print(enemy_ready_message)

# Game loop
running = True

while running:

    action = input('Please enter your action: ')
    s.send(action.encode(FORMAT))
    enemy_status = pickle.loads(s.recv(2048))
    print(f'Enemy Monster Status: {enemy_status}')
    # if enemy_status.isDead():
    #     print('You win!')
    #     break
    # else:
    #     print('You lose!')
    #     break

