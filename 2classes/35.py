import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle(7)

print("Area:", circle1.area())
print("Circumference:", circle1.circumference())