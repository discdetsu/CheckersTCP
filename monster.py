class Monster:

    def __init__(self, name, hp, Atk, Def):
        self.name = name
        self.hp = hp
        self.fullHp = hp
        self.Atk = Atk
        self.Def = Def

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getAtk(self):
        return self.Atk

    def getDef(self):
        return self.Def

    def getFullHp(self):
        return self.fullHp

    def setHp(self, hp):
        self.hp += hp

    def attack(self):

        if ((self.getHp() + self.getDef()) - self.getAtk()) < 0:
            self.setHp(0)
        else:
            self.setHp((self.getHp() + self.getDef()) - self.getAtk())

    def heal(self, amount):
        if amount > self.getFullHp():
            self.setHp(self.getFullHp())
        else:
            self.setHp(amount)

    def isDead(self):

        hp = self.getHp()

        if hp == 0:
            dead = True
        else:
            dead = False

        return dead

    def __repr__(self):
        return f'Monster {self.getName()} Atk: {self.getAtk()} Def: {self.getDef()} ' \
               f'hp: {self.getHp()}/{self.getFullHp()}'