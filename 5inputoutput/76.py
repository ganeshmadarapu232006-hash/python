import csv

file = open("students.csv", "r")

reader = csv.reader(file)

rows = list(reader)

file.close()

student_id = input("Enter student ID to delete: ")

new_rows = []
found = False

for row in rows:
    if row[0] == student_id:
        found = True
    else:
        new_rows.append(row)

file = open("students.csv", "w", newline="")

writer = csv.writer(file)
writer.writerows(new_rows)

file.close()

if found:
    print("Student record deleted successfully.")
else:
    print("Student not found.")