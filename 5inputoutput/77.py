import csv

file = open("students.csv", "r")

reader = csv.reader(file)

next(reader)

highest_marks = -1
topper = []

for row in reader:
    marks = int(row[3])

    if marks > highest_marks:
        highest_marks = marks
        topper = row

file.close()

if topper:
    print("Topper Details:")
    print("Student ID:", topper[0])
    print("Name:", topper[1])
    print("Course:", topper[2])
    print("Marks:", topper[3])
else:
    print("No student records found.")