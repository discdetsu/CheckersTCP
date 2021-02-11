class Monster:

    def __init__(self, name, hp, Atk, Def):
        self.name = name
        self.hp = hp
        self.fullHp = self.hp
        self.Atk = Atk
        self.Def = Def

    def getFullHp(self):
        return self.fullHp

    def attack(self, monster):

        if self.Atk >= (monster.hp + monster.Def):
            monster.hp = 0
        else:
            if (monster.hp + monster.Def) - self.Atk >= monster.getFullHp():
                monster.Def -= self.Atk
            else:
                monster.hp = (monster.hp + monster.Def) - self.Atk



    def heal(self, amount):
        if amount > self.getFullHp():
            self.setHp(self.getFullHp())
        else:
            self.setHp(amount)

    def isDead(self):

        if self.hp == 0:
            dead = True
        else:
            dead = False

        return dead

    def __repr__(self):
        return f'Monster {self.name} Atk: {self.Atk} Def: {self.Def} ' \
               f'hp: {self.hp}/{self.getFullHp()}'
