from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount, transaction_id):
        self.amount = amount
        self.transaction_id = transaction_id

    @abstractmethod
    def make_payment(self):
        pass


# UPI Payment
class UPIPayment(Payment):

    def make_payment(self):
        print("UPI Payment Successful")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)

class CreditCardPayment(Payment):

    def make_payment(self):
        print("Credit Card Payment Successful")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)
class NetBankingPayment(Payment):

    def make_payment(self):
        print("Net Banking Payment Successful")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)

upi = UPIPayment(1000, "UPI101")
card = CreditCardPayment(2000, "CARD102")
netbanking = NetBankingPayment(3000, "NET103")

upi.make_payment()

print()

card.make_payment()

print()

netbanking.make_payment()