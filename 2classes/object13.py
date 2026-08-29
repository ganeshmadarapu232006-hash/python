class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

product1 = Product("Laptop", 50000, 2)
product2 = Product("Mouse", 500, 3)
product3 = Product("Keyboard", 1000, 2)

print("Product 1:", product1.name)
print("Total Price:", product1.total_price())

print("\nProduct 2:", product2.name)
print("Total Price:", product2.total_price())

print("\nProduct 3:", product3.name)
print("Total Price:", product3.total_price())