from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_details(self):
        pass


# Student class
class Student(Person):

    def display_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

class Teacher(Person):

    def display_details(self):
        print("Teacher Name:", self.name)
        print("Teacher Age:", self.age)

class Doctor(Person):

    def display_details(self):
        print("Doctor Name:", self.name)
        print("Doctor Age:", self.age)

student = Student("Ravi", 20)
teacher = Teacher("Suresh", 35)
doctor = Doctor("Anil", 40)

student.display_details()

print()

teacher.display_details()

print()

doctor.display_details()