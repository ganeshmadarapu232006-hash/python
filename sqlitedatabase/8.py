import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

query = "SELECT * FROM students WHERE course = %s"
value = ("Python",)

cursor.execute(query, value)

records = cursor.fetchall()

for student in records:
    print(student)

cursor.close()
con.close()