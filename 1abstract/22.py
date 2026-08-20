from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Car class
class Car(Vehicle):

    def start(self):
        print(self.brand, self.model, "Car started")

    def stop(self):
        print(self.brand, self.model, "Car stopped")


# Bike class
class Bike(Vehicle):

    def start(self):
        print(self.brand, self.model, "Bike started")

    def stop(self):
        print(self.brand, self.model, "Bike stopped")


# Creating objects
car = Car("Toyota", "Camry")
bike = Bike("Honda", "Shine")

# Calling methods
car.start()
car.stop()

print()

bike.start()
bike.stop()