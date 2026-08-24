from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price: ₹", self.price)

class Electronics(Product):

    def calculate_discount(self):
        return self.price * 0.10

class Clothing(Product):

    def calculate_discount(self):
        return self.price * 0.20

laptop = Electronics("Laptop", 50000)
shirt = Clothing("Shirt", 2000)

laptop.display_product()
print("Discount: ₹", laptop.calculate_discount())

print()

shirt.display_product()
print("Discount: ₹", shirt.calculate_discount())