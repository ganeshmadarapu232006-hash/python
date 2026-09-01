class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

student1 = Student("Ganesh", 85)

print("Student Name:", student1.name)
print("Marks:", student1.marks)
print("Grade:", student1.calculate_grade())