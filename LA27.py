from turtle import NinjaTurtle

class Splinter(NinjaTurtle):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @property
    def name(self):
        return self.__alias

splinter = Splinter("Splinter", "Sensei")

print(splinter.name)
