from monster import *
import tkinter as tk


class Game:

    def __init__(self, player1, player2):
        self.turn = 1
        self.player1 = player1
        self.player2 = player2

    def changeTurn(self):
        self.turn *= -1

    def checkWin(self, player1, player2):
        if (player1.isDead()):
            return player2
        else:
            return player1


class Player:

    def __init__(self, monster):
        self.currentTurn = False
        self.monster = monster
