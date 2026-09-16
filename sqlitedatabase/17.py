import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

name = "Ganesh"

query = "SELECT * FROM students WHERE name = %s"

cursor.execute(query, (name,))

records = cursor.fetchall()

if records:
    print("Student(s) found:")
    for student in records:
        print(student)
else:
    print("Student not found!")

cursor.close()
con.close()