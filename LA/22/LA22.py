class BirthdayParty:
    def __init__(self, theme, foods, special_dish):
        self.theme = theme
        self.foods = foods
        self.__special_dish = special_dish
    
    def print_foods(self):
        print(f"Theme: {self.theme}")
        print("Foods:") 
        for food in self.foods:
            print(f"- {food}")
        self.__print_special_dish()
        
    def __print_special_dish(self):
        print(f"Special Dish: {self.__special_dish}")

party1 = BirthdayParty("Tropical", ["Pineapple Pizza", "Fruit Salad","Coconut Water"], "Mango Sorbet")
party2 = BirthdayParty("Retro", ["Burgers", "Fries", "Soda"], "Banana Split")
party3 = BirthdayParty("Space", ["Alien Cupcakes", "Galactic Slush", "Meteor Popcorn"], "Moon Cheesecake")

party1.print_foods()
print("\n")
party2.print_foods()
print("\n")
party3.print_foods()