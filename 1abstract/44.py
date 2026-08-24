from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Balance: ₹", self.balance)

class SavingsAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.05

class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.03

savings = SavingsAccount("SA101", 50000)
current = CurrentAccount("CA102", 75000)

savings.display_balance()
print("Interest: ₹", savings.calculate_interest())

print()

current.display_balance()
print("Interest: ₹", current.calculate_interest())