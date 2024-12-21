class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"My favorite food is {self.name}. It has the following ingredients: {self.ingredients}"

food1 = FavoriteFood("Pizza", "dough, tomato sauce, cheese, pepperoni")
food2 = FavoriteFood("Ice Cream", "milk, cream, sugar, vanilla extract")
food3 = FavoriteFood("Sushi", "rice, seaweed, fish, avocado")

print(food1)
print(food2)
print(food3)