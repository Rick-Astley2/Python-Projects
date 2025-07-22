import random

class Creatures:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        damage = random.randint(self.power - 2, self.power + 2)
        target.health -= damage
        print(f"{self.name} attacked {target.name} dealt {damage} damage!")

    def is_alive(self):
        return self.health > 0
    
class Dragon(Creatures):
    def __init__(self, name):
        super().__init__(name, health=100, power=25)

class Ork(Creatures):
    def __init__(self, name):
        super().__init__(name, health=150, power=15)

class Elf(Creatures):
    def __init__(self, name):
        super().__init__(name, health=80, power=20)

    def heal_(self):
        heal = 5
        self.health += heal
        print(f"{self.name} healed {heal} ")

    def attack(self, target):
        super().attack(target)
        self.heal_()

def battle(c1, c2):
    turn = 0
    while c1.is_alive() and c2.is_alive():
        print(f"\n-- Turn {turn + 1} --\n")
        if turn % 2 == 0:
            c1.attack(c2)
        
        else:
            c2.attack(c1)
        print(f"{c1.name}: {c1.health} HP")
        print(f"{c2.name}: {c2.health} HP")
        turn += 1

    winner = c1 if c1.is_alive() else c2
    print(f"\n {winner.name} wins!")

o = Ork("steve")
e = Elf("herald")
d = Dragon("drago")
battle(e, o)