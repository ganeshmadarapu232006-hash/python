file = open("students.txt", "r")

highest_marks = -1
student_name = ""

for line in file:
    if line.strip().startswith("Name:"):
        student_name = line.strip().split(":")[1].strip()

    if line.strip().startswith("Marks:"):
        marks = int(line.strip().split(":")[1].strip())

        if marks > highest_marks:
            highest_marks = marks
            highest_student = student_name

file.close()

if highest_marks != -1:
    print("Student with highest marks:", highest_student)
    print("Marks:", highest_marks)
else:
    print("No marks found in the file.")