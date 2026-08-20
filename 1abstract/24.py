from abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):

    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass


# SavingsAccount class
class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("Savings Account Interest: 5%")


# CurrentAccount class
class CurrentAccount(BankAccount):

    def calculate_interest(self):
        print("Current Account Interest: 3%")


# Creating objects
savings = SavingsAccount("Ravi", "SA101")
current = CurrentAccount("Manu", "CA102")

# Display details
print("Account Holder:", savings.account_holder)
print("Account Number:", savings.account_number)

savings.calculate_interest()

print("Account Holder:", current.account_holder)
print("Account Number:", current.account_number)
current.calculate_interest()