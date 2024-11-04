(turtle.py)
from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
        return self.__alias

class Michelangelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
        return self.__alias

class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
        return self.__alias

class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
        return self.__alias


(main.py)
from turtles import Leonardo, Michelangelo, Donatello, Raphael

leo = Leonardo("Leonardo", "Leo")
mikey = Michelangelo("Michelangelo", "Mikey")
don = Donatello("Donatello", "Don")
raph = Raphael("Raphael", "Raph")

print(leo.name)
print(mikey.name)
print(don.name)
print(raph.name)