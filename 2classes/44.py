class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def start(self):
        print(self.model, "is starting")

    def stop(self):
        print(self.model, "is stopped")

    def display(self):
        print("Model:", self.model)
        print("Price:", self.price)

car1 = Car("Toyota Innova", 2500000)

car1.start()
car1.display()
car1.stop()