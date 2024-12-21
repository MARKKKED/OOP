class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"This car is a {self.brand}"

car = Car("Toyota")
print(car)
del car
print(car)
