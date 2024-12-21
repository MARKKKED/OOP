class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

    def modify_price(self, new_price):
        self.price = new_price

def create_phone():
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = float(input("Enter phone price: "))
    return Phone(brand, model, price)

def modify_phone(phones):
    print("Available Phones:")
    for i, phone in enumerate(phones):
        print(f"{i + 1}. {phone}")

    choice = int(input("Enter the number of the phone to modify: ")) - 1
    if 0 <= choice < len(phones):
        new_price = float(input("Enter the new price: "))
        phones[choice].modify_price(new_price)
        print("Phone price modified successfully.")
    else:
        print("Invalid choice.")

def delete_phone(phones):
    print("Available Phones:")
    for i, phone in enumerate(phones):
        print(f"{i + 1}. {phone}")

    choice = int(input("Enter the number of the phone to delete: ")) - 1
    if 0 <= choice < len(phones):
        del phones[choice]
        print("Phone deleted successfully.")
    else:
        print("Invalid choice.")

def main():
    phones = []

    while True:
        print("\nPhone Management System")
        print("1. Create Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. View Phones")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            phones.append(create_phone())
        elif choice == '2':
            modify_phone(phones)
        elif choice == '3':
            delete_phone(phones)
        elif choice == '4':
            if phones: 
                print("Available Phones:")
                for phone in phones:
                    print(phone)
            else:
                print("No phones available.")
        elif choice == '5':
            print("Exiting the Phone Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()