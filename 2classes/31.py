class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student1 = Student("Ganesh", 20, "Python")

student1.display()