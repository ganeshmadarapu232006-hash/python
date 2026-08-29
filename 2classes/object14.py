class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

car1 = Car("Toyota", "Fortuner", 2024, 4000000)
car2 = Car("Honda", "City", 2023, 1500000)
car3 = Car("BMW", "X5", 2025, 8500000)

print("Car 1:")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Year:", car1.year)
print("Price:", car1.price)

print("\nCar 2:")
print("Brand:", car2.brand)
print("Model:", car2.model)
print("Year:", car2.year)
print("Price:", car2.price)

print("\nCar 3:")
print("Brand:", car3.brand)
print("Model:", car3.model)
print("Year:", car3.year)
print("Price:", car3.price)