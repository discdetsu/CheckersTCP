import socket
from monster import Monster
import pickle
import tkinter as tk
from tkinter import *

print('!!!!   Monster Fight  !!!!')

HOST = 'localhost'
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

# UI
# def onclick1():
#     monster.Atk
#
# def onclick2():
#     monster.heal((monster.getFullHp()*30)//100)
#
# root = Tk()
# root.title("Monster Fight")
# photo = PhotoImage(file="spider2.png")
# Button(root, image=photo).pack()
# ATKButton = Button(root, text="Attack", commmand=onclick1)
# ATKButton.pack()
# HEALButton = Button(root, text="HEAL",command=onclick2)
# HEALButton.pack()
# Label=(root)
#
#
# root.mainloop()


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
enemy_ready_message = s.recv(1024).decode(FORMAT)
print(enemy_ready_message)

# Game loop
running = True

while running:
    action = input('Please enter your action: ')
    s.send(action.encode(FORMAT))
    enemy_action = s.recv(1024).decode(FORMAT)
    print(f'Received: {enemy_action}')

# data = pickle.dumps(monster)
# s.send(data)


# while running:
#
#     if msg == 'q':
#         break
#     else:
#         # Send data to server
#         s.send(msg.encode(FORMAT))
#
#     # Received data from the server
#     data = s.recv(1024).decode(FORMAT)
#     print('Received: ', data)
