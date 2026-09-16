import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

student_id = 1

query = "SELECT * FROM students WHERE id = %s"

cursor.execute(query, (student_id,))

student = cursor.fetchone()

if student:
    print("Student found!")
    print("ID:", student[0])
    print("Name:", student[1])
    print("Age:", student[2])
    print("Course:", student[3])
    print("Marks:", student[4])
else:
    print("Student not found!")

cursor.close()
con.close()