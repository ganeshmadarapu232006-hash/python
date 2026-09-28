import json

file = open("student.json", "r")

students = json.load(file)

file.close()

student_id = input("Enter student ID to delete: ")

found = False

for student in students:
    if str(student["Student ID"]) == student_id:
        students.remove(student)
        found = True
        break

if found:
    file = open("student.json", "w")

    json.dump(students, file, indent=4)

    file.close()

    print("Student deleted successfully.")
else:
    print("Student not found.")