class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Ganesh", 20, "CCN")
student2 = Student("Rahul", 19, "CSE")
student3 = Student("Kiran", 20, "ECE")

print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)

print("\nStudent 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Course:", student2.course)

print("\nStudent 3:")
print("Name:", student3.name)
print("Age:", student3.age)
print("Course:", student3.course)