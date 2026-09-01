class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

student1 = Student("Ganesh", [80, 75, 90, 85, 70])

print("Student Name:", student1.name)
print("Total Marks:", student1.total_marks())
print("Average Marks:", student1.average_marks())