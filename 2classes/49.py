class Laptop:
    def __init__(self, brand, model, processor, ram, storage, price):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Laptop Specifications")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Processor:", self.processor)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)

laptop1 = Laptop(
    "Dell",
    "Inspiron 15",
    "Intel Core i5",
    "8 GB",
    "512 GB SSD",
    55000
)

laptop1.display()