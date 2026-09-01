class Student:
    
    college_name = "Aditya Polytechnic College"

    def __init__(self, name):
        self.name = name

student1 = Student("Ganesh")
student2 = Student("Ravi")
student3 = Student("Manoj")

print("Student Name:", student1.name)
print("College Name:", student1.college_name)

print("\nStudent Name:", student2.name)
print("College Name:", student2.college_name)

print("\nStudent Name:", student3.name)
print("College Name:", student3.college_name)