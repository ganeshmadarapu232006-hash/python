import csv

file = open("students.csv", "r")

reader = csv.reader(file)

header = next(reader)
students = list(reader)

file.close()

students.sort(key=lambda row: int(row[3]), reverse=True)

file = open("sorted_students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow(header)

writer.writerows(students)

file.close()

print("Student records sorted and saved successfully.")