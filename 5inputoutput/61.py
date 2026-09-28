file = open("student.txt", "w")

name = input("Enter student name: ")
age = input("Enter age: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Course: " + course + "\n")
file.write("Marks: " + marks + "\n")

print("Student details saved successfully.")

file.close()