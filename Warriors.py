from random import randint as ri
from time import sleep


class Warrior():
    def __init__(self):
        self.hp = 100
        self.damage = ri(5, 15)
        self.isAlive = True

    def get_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        if self.hp <= 0:
            self.isAlive = False

    def hill(self, hp_hill):
        self.hp += hp_hill

    def up_damage(self):
        self.damage += 3

    def level_up(self):
        self.hp += 10
        self.damage += 4

    def set_name(self, name):
        self.name = name



warrior1 = Warrior()
warrior2 = Warrior()
round_kol = 1

print("Name first warrior:")
warrior1.set_name(str(input()))
print("Name second warrior:")
warrior2.set_name(str(input()))


while warrior1.isAlive and warrior2.isAlive:
    print("---", round_kol, " round-------------------", sep="")
    round_kol += 1

    act = ri(1, 3)                              #действие 1
    if act == 1:
        hp_hill = ri(5,25)
        warrior1.hill(ri(5,25))
        print(warrior1.name, "hill", hp_hill)
    elif act == 2:
        warrior1.level_up()
        print(warrior1.name, "raised his level")
    elif act == 3:
        warrior1.up_damage()
        print(warrior1.name, "damage increased to", warrior1.damage)

    act = ri(1, 3)
    if act == 1:                                #действие 2
        hp_hill = ri(5,25)
        warrior2.hill(ri(5,25))
        print(warrior2.name, "hill", hp_hill)
    elif act == 2:
        warrior2.level_up()
        print(warrior2.name, "raised his level")
    elif act == 3:
        warrior2.up_damage()
        print(warrior2.name, "damage increased to", warrior2.damage)

    warrior1.get_damage(warrior2.damage)
    print(warrior1.name, "took", warrior2.damage, "damage")
    print(warrior1.name, "lost", warrior1.hp, "HP")

    if warrior1.isAlive == False:
        print(warrior1.name, "died")
        print(warrior2.name, "won")
        break

    warrior2.get_damage(warrior1.damage)
    print(warrior2.name, "took", warrior1.damage, "damage")
    print(warrior2.name, "lost", warrior2.hp, "HP")

    if warrior2.isAlive == False:
        print(warrior2.name, "died")
        print(warrior1.name, "won")
        break

    sleep(5)
    pass
