class Car:
    def __init__(self, car_number, car_model, car_name):
        self.car_number = car_number
        self.car_model = car_model
        self.car_name = car_name

car1 = Car(101, "Toyota", "Fortuner")
car2 = Car(102, "Honda", "City")
car3 = Car(103, "BMW", "X5")

print(car1.car_number, car1.car_model, car1.car_name)
print(car2.car_number, car2.car_model, car2.car_name)
print(car3.car_number, car3.car_model, car3.car_name)