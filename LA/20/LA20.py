class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self.__ingredients = ingredients

    def display_info(self):
        return f"{self.name} includes the ingredients: {self.__ingredients}."

    def get_ingredients(self):
        return self.__ingredients

food1 = FavoriteFood("Pizza", "dough, tomato sauce, cheese, pepperoni")
food2 = FavoriteFood("Ice Cream", "milk, cream, sugar, vanilla extract")
food3 = FavoriteFood("Sushi", "rice, seaweed, fish, avocado")

print(food1.display_info())
print(food2.display_info())
print(food3.display_info())

