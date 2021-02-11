import socket
from monster import Monster
import pickle

print('!!!!   Monster Fight  !!!!')
print('Create monster!')

HOST = 'localhost'
PORT = 5555

# Create socket object
# socket.SOCK_STREAM = TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the server
s.connect((HOST, PORT))

name = input('''Pleas enter your monster's name: ''')
hp = int(input('Health point: '))
atk = int(input('Attack damage: '))
deff = int(input('Defense point: '))

# monster = Monster(name, hp, atk, deff)
# data_stream = pickle.dumps(monster)
# s.send(data_stream)

def main():
    # Game loop
    running = True



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
