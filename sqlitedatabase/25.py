import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

course = input("Enter course name: ")

query = "SELECT * FROM students WHERE course = %s"

cursor.execute(query, (course,))

records = cursor.fetchall()

if records:
    print("\nStudents in", course, "course:")
    for student in records:
        print(student)
else:
    print("No students found in this course.")

cursor.close()
con.close()