import socket
from monster import Monster
from _thread import *
import threading
import pickle
from time import *

HOST = '158.108.213.72'
PORT = 5555
FORMAT = 'utf-8'

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
        print(f'Player 2 connected form port {p2Address}')
        break

print('Both players are connected')
sleep(1)
print('Waiting for players to ready up...')
s.setblocking(False)


while True:

    try:
        p1_monster = pickle.loads(p1Connection.recv(2048))
        print(f'Player 1 {p1_monster}')
    except socket.error as e:
        print(e)

    try:
        p2_monster = pickle.loads(p2Connection.recv(2048))
        print(f'Player 2 {p2_monster}')
    except socket.error as e:
        print(e)

    p2Connection.send(str('Your enemy is ready').encode(FORMAT))
    p1Connection.send(str('Your enemy is ready').encode(FORMAT))
    print('Sending start to both players')

    break


# Event loop
turn = 1
roundCount = 1

while True:

    if turn == 1:

        try:
            p1_action = p1Connection.recv(2048).decode(FORMAT)
            print(f'Received: {p1_action}')
        except:
            pass

        if p2_monster.isDead():
            print(f'The winner is ........ {p1_monster}')
            p1_monster.win = True
            break

        if p1_action == 'A':
            print(f'Player 1 Attack with damage dealt: {p1_monster.Atk}')
            p1_monster.attack(p2_monster)
        elif p1_action == 'H':
            amount = 10
            print(f'Player 1 Heal with amount: {amount}')
            p1_monster.heal(amount)
        turn *= -1


    if turn == -1:
        try:
            p2_action = p2Connection.recv(2048).decode(FORMAT)
            print(f'Received: {p2_action}')
        except:
            pass

        if p1_monster.isDead():
            print(f'The winner is ........ {p2_monster}')
            p2_monster.win = True
            break

        if p2_action == 'A':
            print(f'Player 2 Attack with damage dealt: {p2_monster.Atk}')
            p2_monster.attack(p1_monster)

        elif p2_action[0] == 'H':
            amount = 10
            print(f'Player 2 Heal with amount: {amount}')
            p2_monster.heal(amount)
        turn *= -1

    p2Connection.send(pickle.dumps(p1_monster))
    p1Connection.send(pickle.dumps(p2_monster))


p1Connection.close()
p2Connection.close()

print('Closed sockets')


