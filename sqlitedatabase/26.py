import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

min_marks = int(input("Enter minimum marks: "))
max_marks = int(input("Enter maximum marks: "))

query = """
SELECT * FROM students
WHERE marks BETWEEN %s AND %s
"""

values = (min_marks, max_marks)

cursor.execute(query, values)

records = cursor.fetchall()

if records:
    print("\nStudents with marks between", min_marks, "and", max_marks, ":")
    for student in records:
        print(student)
else:
    print("No students found!")

cursor.close()
con.close()