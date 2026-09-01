class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")

account1 = BankAccount("Ganesh", 10000)

account1.deposit(5000)
account1.withdraw(3000)