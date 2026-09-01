class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("Laptop", 50000)
product2 = Product("Mobile", 20000)
product3 = Product("Headphones", 2000)

print("Product 1:", product1.name, product1.price, product1.category)
print("Product 2:", product2.name, product2.price, product2.category)
print("Product 3:", product3.name, product3.price, product3.category)