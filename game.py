from monster import *

class Game:
    def __init__(self, id):
        self.p1Ready = False
        self.p2Ready = False
        self.ready = False
        self.id = id

# Create Monster
print('===Player1===')
name1 = input('''Pleas enter your monster's name: ''')
hp1 = int(input('Health point: '))
atk1 = int(input('Attack damage: '))
deff1 = int(input('Defense point: '))
m1 = Monster(name1, hp1, atk1, deff1)
print('')
print('===Player2===')
name2 = input('''Pleas enter your monster's name: ''')
hp2 = int(input('Health point: '))
atk2 = int(input('Attack damage: '))
deff2 = int(input('Defense point: '))
m2 = Monster(name2, hp2, atk2, deff2)
print('')


# Turn count
turn = 1
round = 1

# Game loop

while True:

    print(f'Round: {round}')

    if turn == 1:
        print(f'>>> Monster {m1.name} turn <<<')
        action = input('Please enter skill A=attack H=heal: ')
        if action == 'A':
            m1.attack(m2)
        elif action == 'H':
            heal_amount = int(input('Please enter recovery hp[1-10]: '))
            if heal_amount < 1 or heal_amount > 10:
                continue
            m1.heal(heal_amount)
        print(m1)
        print(m2)
        turn *= -1

        if m2.isDead():
            print(f'The winner is ........ {m1}')
            break

    elif turn == -1:
        print(f'>>> Monster {m2.name} turn <<<')
        action = input('Please enter skill A=attack H=heal: ')
        if action == 'A':
            m2.attack(m1)
        elif action == 'H':
            heal_amount = int(input('Please enter recovery hp[1-10]: '))
            if heal_amount < 1 or heal_amount > 10:
                continue
            m2.heal(heal_amount)
        print(m1)
        print(m2)
        turn *= -1

        if m2.isDead():
            print(f'The winner is ........ {m1.name}')
            break

    round += 1
    print('')

# class Player:
#
#     def __init__(self, monster):
#         self.currentTurn = False
#         self.monster = monster
