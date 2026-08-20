from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle("Red", 10, 5)
circle = Circle("Blue", 7)

print("Rectangle Color:", rectangle.color)
print("Rectangle Area:", rectangle.area())

print()

print("Circle Color:", circle.color)
print("Circle Area:", circle.area())