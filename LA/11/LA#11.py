class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"Brand: {self.brand} \nModel: {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        super().__init__(brand, model)

android = Android("Samsung", "Galaxy S24 Ultra")
android.describePhone()