class Student:
    def __init__(self, name):
        self.name = name

student = Student("Ganesh")

try:
    print(student.age)

except AttributeError:
    print("Error: The attribute does not exist.")