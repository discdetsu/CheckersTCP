import socket
from monster import Monster
import pickle

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

name = input('''Please enter your monster's name: ''')
hp = int(input('Health point: '))
atk = int(input('Attack damage: '))
deff = int(input('Defense point: '))

monster = Monster(name, hp, atk, deff)
data = pickle.dumps(monster)
s.send(data)


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
