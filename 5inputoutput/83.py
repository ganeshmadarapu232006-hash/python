import json
import os

if os.path.exists("students.json"):
    file = open("students.json", "r")
    data = json.load(file)
    file.close()

    if isinstance(data, dict):
        students = [data]
    else:
        students = data
else:
    students = []

student_id = input("Enter student ID: ")
name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
marks = int(input("Enter marks: "))

new_student = {
    "Student ID": student_id,
    "Name": name,
    "Age": age,
    "Course": course,
    "Marks": marks
}

students.append(new_student)

file = open("students.json", "w")

json.dump(students, file, indent=4)

file.close()

print("Student added successfully.")