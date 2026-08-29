class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

laptop1 = Laptop("Dell", "16GB", "Intel i5", 65000)

print("Laptop Details:")
print("Brand:", laptop1.brand)
print("RAM:", laptop1.ram)
print("Processor:", laptop1.processor)
print("Price:", laptop1.price)