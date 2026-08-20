from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")

class CreditCard(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")

class NetBanking(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Net Banking")

payments = [
    UPI(),
    CreditCard(),
    NetBanking()
]

for payment in payments:
    payment.pay(1000)