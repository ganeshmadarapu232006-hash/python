class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

product1 = Product("Laptop", 50000, 2)

print("Product Information:")
print("Product Name:", product1.product_name)
print("Price:", product1.price)
print("Quantity:", product1.quantity)