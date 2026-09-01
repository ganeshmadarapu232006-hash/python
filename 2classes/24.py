class Car:
    number_of_wheels = 4  

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Number of Wheels:", Car.number_of_wheels)
        
car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")
car3 = Car("Hyundai", "Creta")

car1.display()
car2.display()
car3.display()