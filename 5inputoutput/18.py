name = input("Enter student name: ")
age = input("Enter student age: ")
course = input("Enter student course: ")

with open("students.txt", "a") as file:
    file.write("\nName: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Course: " + course + "\n")

print("Student details added successfully.")