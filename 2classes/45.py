class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

account1 = BankAccount("Ganesh", "1234567890", 10000)

print("Account Holder:", account1.account_holder)
print("Account Number:", account1.account_number)
print("Initial Balance:", account1.balance)