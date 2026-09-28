import csv

file = open("students.csv", "a", newline="")

writer = csv.writer(file)

student_id = input("Enter student ID: ")
name = input("Enter name: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

writer.writerow([student_id, name, course, marks])

print("New student record added successfully.")

file.close()