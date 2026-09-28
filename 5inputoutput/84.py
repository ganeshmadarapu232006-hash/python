import json

file = open("student.json", "r")

data = json.load(file)

file.close()

if isinstance(data, dict):
    students = [data]
else:
    students = data

student_id = input("Enter student ID to update: ")

found = False

for student in students:

    if str(student["Student ID"]) == student_id:

        print("Enter new details:")

        student["Name"] = input("Enter new name: ")
        student["Age"] = int(input("Enter new age: "))
        student["Course"] = input("Enter new course: ")
        student["Marks"] = int(input("Enter new marks: "))

        found = True
        break

if found:
    file = open("student.json", "w")

    json.dump(students, file, indent=4)

    file.close()

    print("Student information updated successfully.")

else:
    print("Student not found.")