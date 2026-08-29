class BankAccount:
    def __init__(self, account_holder_name, account_number):
        self.account_holder_name = account_holder_name
        self.account_number = account_number

account1 = BankAccount("Ganesh", 123456789)

print("Bank Account Details:")
print("Account Holder Name:", account1.account_holder_name)
print("Account Number:", account1.account_number)