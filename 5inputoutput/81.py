import json

student_id = input("Enter student ID: ")
name = input("Enter name: ")
age = input("Enter age: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

student = {
    "Student ID": student_id,
    "Name": name,
    "Age": age,
    "Course": course,
    "Marks": marks
}

file = open("student.json", "w")

json.dump(student, file, indent=4)

file.close()

print("Student information saved successfully.")