class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

account1 = BankAccount("Ganesh", "1234567890", 25000)
account2 = BankAccount("Rahul", "9876543210", 40000)

account1.display()
account2.display()