import csv

file = open("students.csv", "r")

reader = csv.reader(file)

next(reader)

print("Students who scored below 40:")

for row in reader:
    marks = int(row[3])

    if marks < 40:
        print("Student ID:", row[0])
        print("Name:", row[1])
        print("Course:", row[2])
        print("Marks:", row[3])

file.close()