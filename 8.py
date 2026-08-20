from abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("Savings Account: Interest calculated at 4%")

class CurrentAccount(BankAccount):

    def calculate_interest(self):
        print("Current Account: Interest calculated at 2%")

savings = SavingsAccount()
current = CurrentAccount()
savings.calculate_interest()
current.calculate_interest()