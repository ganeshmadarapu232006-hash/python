# Create a file and write name, age, and course

name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Course: " + course + "\n")

print("Details saved successfully.")