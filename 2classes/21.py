class Student:
    college_name = "Aditya Polytechnic College"   # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college_name)

student1 = Student("Ganesh", 20)
student2 = Student("Ravi", 21)
student3 = Student("Kiran", 20)

student1.display()
student2.display()
student3.display()