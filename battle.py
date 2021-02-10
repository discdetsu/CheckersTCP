import  monster
class Battle_control:
 p1 = monster.Monster('A1',200,50,10)
 p2 = monster.Monster('A2',200,20,40)
 def fight(p1,p2):
      Battle_control.p1.hp = Battle_control.p1.getHp() - (Battle_control.p2.getAtk() - Battle_control.p1.getDef())
      Battle_control.p2.hp = Battle_control.p2.getHp() - (Battle_control.p1.getAtk() - Battle_control.p2.getDef())

