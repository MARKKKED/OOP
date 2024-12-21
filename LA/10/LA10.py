class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"Brand: {self.brand} \nModel: {self.model} \nFuel Type: {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

car = Car("Toyota", "Corolla", "Gasoline")
motor = Motorcycle("Yamaha", "MT-07", "Gasoline")

print("Car Details:")
car.describeVehicle()
print("\nMotorcycle Details:")
motor.describeVehicle()
