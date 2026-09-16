import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

cursor.execute("SELECT name FROM students")

records = cursor.fetchall()

for student in records:
    print(student[0])

cursor.close()
con.close()