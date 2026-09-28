import csv

file = open("students.csv", "r")

reader = csv.reader(file)

rows = list(reader)

file.close()

student_id = input("Enter student ID: ")
new_marks = input("Enter new marks: ")

found = False

for row in rows:
    if row[0] == student_id:
        row[3] = new_marks
        found = True
        break

file = open("students.csv", "w", newline="")

writer = csv.writer(file)
writer.writerows(rows)

file.close()

if found:
    print("Marks updated successfully.")
else:
    print("Student not found.")