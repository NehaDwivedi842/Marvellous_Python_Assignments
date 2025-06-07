class BankAccount:
    ROI = 10.5 
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self, deposit_amt):
        self.Amount += deposit_amt
        print(f"{deposit_amt} deposited successfully.")

    def Withdraw(self, withdraw_amt):
        if withdraw_amt > self.Amount:
            print("Insufficient balance.")
        else:
            self.Amount -= withdraw_amt
            print(f"{withdraw_amt} withdrawn successfully.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest on current amount:", interest)

def main():
    acc1 = BankAccount("Alice", 1000)
    acc2 = BankAccount("Bob", 2000)

    acc1.Display()
    acc1.Deposit(500)
    acc1.Withdraw(300)
    acc1.CalculateInterest()
    acc1.Display()

    acc2.Display()
    acc2.Deposit(1000)
    acc2.Withdraw(500)
    acc2.CalculateInterest()
    acc2.Display()


if __name__ == "__main__":
    main()