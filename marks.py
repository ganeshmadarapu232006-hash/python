# Student Marks Calculator

print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

python = float(input("Enter Python marks: "))
java = float(input("Enter Java marks: "))
mysql = float(input("Enter MySQL marks: "))
html = float(input("Enter HTML marks: "))
css = float(input("Enter CSS marks: "))

total = python + java + mysql + html + css
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== STUDENT MARKS REPORT =====")
print("Name:", name)
print("Roll No:", roll_no)
print("Python:", python)
print("Java:", java)
print("MySQL:", mysql)
print("HTML:", html)
print("CSS:", css)
print("Total:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("================================")