import csv

file = open("students.csv", "r")

reader = csv.reader(file)

next(reader)

total = 0
count = 0

for row in reader:
    marks = int(row[3])
    total += marks
    count += 1

file.close()

if count > 0:
    average = total / count
    print("Average marks:", average)
else:
    print("No student records found.")