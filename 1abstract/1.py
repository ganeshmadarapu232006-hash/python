from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        print("Animal sounds")

class Dog(Animal):

    def sound(self):
        print("Dog is barking")


# Cat class
class Cat(Animal):

    def sound(self):
        print("Cat makes a sound")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()