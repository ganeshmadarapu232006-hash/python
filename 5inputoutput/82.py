import json

file = open("student.json", "r")

student = json.load(file)

print("Student ID:", student["Student ID"])
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Course:", student["Course"])
print("Marks:", student["Marks"])

file.close()