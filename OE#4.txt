class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}, reducing their health to {target.health}")

    def special_move(self):
        pass

class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash! Their attack power is doubled for the next attack.")
        self.power *= 2

class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball! {self.name} reduces the target's health by 100 points.")
        self.attack(target)

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow! {self.name} ignores the target's defense and deals direct damage.")
        self.attack(target)

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50

warrior = Warrior("Warrior", 100, 20)
mage = Mage("Mage", 100, 15)
archer = Archer("Archer", 100, 25)
monster = Monster("Monster", 150, 30)

characters = [warrior, mage, archer, monster]
for attacker in characters:
    for target in characters:
        if attacker != target:
            attacker.attack(target)
            attacker.special_move()
            if isinstance(target, Monster):
                target.special_move()

for character in characters:
    character.special_move()