from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print("UPI Payment of ₹", amount, "successful")

    def refund(self, amount):
        print("UPI Refund of ₹", amount, "successful")

class CreditCard(Payment):

    def pay(self, amount):
        print("Credit Card Payment of ₹", amount, "successful")

    def refund(self, amount):
        print("Credit Card Refund of ₹", amount, "successful")


class NetBanking(Payment):

    def pay(self, amount):
        print("Net Banking Payment of ₹", amount, "successful")

    def refund(self, amount):
        print("Net Banking Refund of ₹", amount, "successful")

upi = UPI()
credit_card = CreditCard()
net_banking = NetBanking()

upi.pay(1000)
upi.refund(500)

credit_card.pay(2000)
credit_card.refund(1000)

net_banking.pay(3000)
net_banking.refund(1500)