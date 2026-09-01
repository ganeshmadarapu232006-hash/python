class BankAccount:
    bank_name = "SBI" 

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Bank Name:", BankAccount.bank_name)

account1 = BankAccount("Ganesh", 101, 25000)
account2 = BankAccount("Ravi", 102, 30000)
account3 = BankAccount("Kiran", 103, 40000)

account1.display()
account2.display()
account3.display()