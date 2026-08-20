from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def role(self):
        pass

class Student(Person):

    def role(self):
        print("Student studies and attends classes")

class Teacher(Person):

    def role(self):
        print("Teacher teaches and guides students")

student = Student()
teacher = Teacher()
student.role()
teacher.role()