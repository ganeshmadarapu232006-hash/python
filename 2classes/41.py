class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

student1 = Student("Ganesh", 20, "Python", 85)

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)
print("Marks:", student1.marks)