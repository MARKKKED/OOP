class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("\nKeeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("\nHeating food!")

washer = WashingMachine("LG", "T2021")
fridge = Refrigerator("Samsung", "R456")
microwave = Microwave("Panasonic", "M789")

appliances = [washer, fridge, microwave]

for appliance in appliances:
    appliance.operate()
    appliance.info()