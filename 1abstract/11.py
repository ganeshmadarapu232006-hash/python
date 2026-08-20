from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts with engine")

    def stop(self):
        print("Car is stopping")

class Bike(Vehicle):

    def start(self):
        print("Bike starts with engine")

    def stop(self):
        print("Bike is stopping")

car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()