from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount
    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Payment Amount: ₹", self.amount)

class UPI(Payment):

    def pay(self):
        print("Payment made using UPI")
class CreditCard(Payment):

    def pay(self):
        print("Payment made using Credit Card")

upi = UPI(1000)
card = CreditCard(2000)

upi.display_amount()
upi.pay()
card.display_amount()
card.pay()