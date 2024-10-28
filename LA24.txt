from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print("Swings sword!")

class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")

class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")

class Healer(GameCharacter):
    def attack(self):
        print("Casts healing spell on ally!")

warrior = Warrior()
mage = Mage()
archer = Archer()
healer = Healer()

characters = [warrior, mage, archer, healer]
for character in characters:
    character.attack()