file = open("students.txt", "r")

highest_marks = -1
top_student = ""

lines = file.readlines()

for i in range(len(lines)):
    if lines[i].startswith("Marks:"):
        marks = int(lines[i].strip().split(":")[1].strip())

        if marks > highest_marks:
            highest_marks = marks
            top_student = lines[i - 3].strip()

print("Student with highest marks:")
print(top_student)
print("Marks:", highest_marks)

file.close()