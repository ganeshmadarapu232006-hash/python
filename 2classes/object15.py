class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person1 = Person("Ganesh", 20, "Rajahmundry")
person2 = Person("Rahul", 21, "Hyderabad")

print("Person 1:")
print("Name:", person1.name)
print("Age:", person1.age)
print("City:", person1.city)

print("\nPerson 2:")
print("Name:", person2.name)
print("Age:", person2.age)
print("City:", person2.city)