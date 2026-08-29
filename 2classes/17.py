class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)
        
laptop1 = Laptop("Dell", "8GB", "512GB SSD", 55000)
laptop2 = Laptop("HP", "16GB", "1TB SSD", 70000)
laptop3 = Laptop("Lenovo", "8GB", "256GB SSD", 45000)

laptop1.display()
laptop2.display()
laptop3.display()