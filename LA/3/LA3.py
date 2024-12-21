class MLHero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def describe_MLhero(self):
        print(f"{self.name} is a {self.role} hero.")

hero1 = MLHero("Layla", "Marksman")
hero1.describe_MLhero()