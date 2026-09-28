import json

student = {
    "Student ID": 101,
    "Name": "Ganesh",
    "Age": 20,
    "Course": "CCN",
    "Marks": 85
}

file = open("student.json", "w")

json.dump(student, file, indent=4)

file.close()

print("Student data converted to JSON successfully.")