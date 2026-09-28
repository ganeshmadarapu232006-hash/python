import csv

file = open("students.csv", "r")

reader = csv.reader(file)

next(reader)

student_id = input("Enter student ID to search: ")

found = False

for row in reader:
    if row[0] == student_id:
        print("Student found:")
        print("Student ID:", row[0])
        print("Name:", row[1])
        print("Course:", row[2])
        print("Marks:", row[3])
        found = True
        break

if not found:
    print("Student not found.")

file.close()