from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def display_details(self):
        pass

class SavingsAccount(Account):

    def display_details(self):
        print("Savings Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

class CurrentAccount(Account):

    def display_details(self):
        print("Current Account")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


savings = SavingsAccount("SA101", 50000)
current = CurrentAccount("CA102", 75000)
savings.display_details()

print()

current.display_details()