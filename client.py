import socket
from monster import Monster
import pickle
import tkinter as tk
from tkinter import *

print('!!!!   Monster Fight  !!!!')

HOST = 'localhost'
PORT = 5555

# Create socket object
# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the server
s.connect((HOST, PORT))
print('Connected to server')
print('Create monster!')
# data = s.recv(2048).decode('utf-8')
# print(data)

#UI
def onclick1():
    monster.Atk

def onclick2():
    monster.heal((monster.getFullHp()*30)//100)

root = Tk()
root.title("Monster Fight")
photo = PhotoImage(file="spider2.png")
Button(root, image=photo).pack()
ATKButton = Button(root, text="Attack", commmand=onclick1)
ATKButton.pack()
HEALButton = Button(root, text="HEAL",command=onclick2)
HEALButton.pack()
Label=(root)


root.mainloop()

name = input('''Please enter your monster's name: ''')
hp = int(input('Health point: '))
atk = int(input('Attack damage: '))
deff = int(input('Defense point: '))
monster = Monster(name, hp, atk, deff)

s.send('ready'.encode('utf-8'))
print('sending ready to server')
start = s.recv(1024).decode('utf-8')
print(start)

while True:
    # dumped_monster = pickle.dumps(monster)
    # s.send(dumped_monster)

    command = input('Please enter your command: ')
    s.send(command.encode('utf-8'))
    enemy_command = s.recv(1204).decode('utf-8')
    print(f'Received: {enemy_command}')


# data = pickle.dumps(monster)
# s.send(data)


# def main():
#     # Game loop
#     running = True



# while running:
#
#     if msg == 'q':
#         break
#     else:
#         # Send data to server
#         s.send(msg.encode('utf-8'))
#
#     # Received data from the server
#     data = s.recv(1024).decode('utf-8')
#     print('Received: ', data)
