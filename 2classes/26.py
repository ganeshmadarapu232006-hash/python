class Student:
    object_count = 0

    def __init__(self, name):
        self.name = name

        Student.object_count += 1

student1 = Student("Ganesh")
student2 = Student("Ravi")
student3 = Student("Manoj")
student4 = Student("Kiran")

print("Total objects created:", Student.object_count)