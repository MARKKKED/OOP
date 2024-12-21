class MLHero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def describe(self):
        return f"{self.name} is a {self.role} hero."

hero1 = MLHero("Layla", "Marksman")
print(hero1.describe())