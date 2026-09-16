import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

cursor.execute("SELECT COUNT(*) FROM students")

result = cursor.fetchone()

print("Total number of students:", result[0])

cursor.close()
con.close()