class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Current Balance: {self.__balance}")

    def __display_balance(self):
        print(f"Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
            print(f"Balance set to: {self.__balance}")
        else:
            print("Invalid balance. Must be a non-negative number.")

account = BankAccount("123456789", 1000.0)
account.deposit(500)
account.withdraw(200)
account.set_balance(-50)
account.display_account_info()
