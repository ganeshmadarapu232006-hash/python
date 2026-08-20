from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

class Electronics(Product):

    def calculate_discount(self):
        return self.price * 0.10

class Clothing(Product):

    def calculate_discount(self):
        return self.price * 0.20

laptop = Electronics("Laptop", 50000)
shirt = Clothing("Shirt", 2000)

print("Product Name:", laptop.product_name)
print("Price:", laptop.price)
print("Discount:", laptop.calculate_discount())

print("Product Name:", shirt.product_name)
print("Price:", shirt.price)
print("Discount:", shirt.calculate_discount())