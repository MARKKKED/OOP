class MobileLegendsHero:
    def __init__(self, name, role, damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"Name: {self.name}\nRole: {self.role}\nDamage Type: {self.damage_type}"

    def print_hero_details(self):
        print(f"Hero Details:\n{self}")


hero1 = MobileLegendsHero("Alucard", "Fighter", "Physical")
hero2 = MobileLegendsHero("Harley", "Mage", "Magical")
hero3 = MobileLegendsHero("Johnson", "Tank", "Physical")
hero4 = MobileLegendsHero("Karina", "Assassin", "Physical")
hero5 = MobileLegendsHero("Layla", "Marksman", "Physical")

print("Hero 1:")
hero1.print_hero_details()
print("\nHero 2:")
hero2.print_hero_details()
print("\nHero 3:")
hero3.print_hero_details()
print("\nHero 4:")
hero4.print_hero_details()
print("\nHero 5:")
hero5.print_hero_details()