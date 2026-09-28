import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(["Student ID", "Name", "Course", "Marks"])

n = int(input("Enter number of students: "))

for i in range(n):
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")

    writer.writerow([student_id, name, course, marks])

print("Student CSV file created successfully.")

file.close()