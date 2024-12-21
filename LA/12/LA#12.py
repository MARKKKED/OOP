class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_details(self):
        print(f"Toy Name: {self.name} \nPrice: {self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

toy = Car("Race Car", "$10.99")
toy.display_details()