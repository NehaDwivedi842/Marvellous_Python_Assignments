class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

    def display(self):
        print("Account: ",self.account_number)
        print("Name:",self.name)
        print("Balance: ",self.balance)


acc = BankAccount(123456, "Neha", 10000)
acc.deposit(5000)
acc.withdraw(3000)
acc.display()
