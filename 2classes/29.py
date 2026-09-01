class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):

        self.model = model
        self.price = price

car1 = Car("Innova", 2500000)
car2 = Car("Fortuner", 4000000)
car3 = Car("Glanza", 1000000)

print("Company:", Car.company)
print("Number of Wheels:", Car.number_of_wheels)

print("Car 1:", car1.model, car1.price)
print("Car 2:", car2.model, car2.price)
print("Car 3:", car3.model, car3.price)