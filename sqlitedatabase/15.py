import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

query = "DELETE FROM students WHERE id = %s"

student_id = 1

cursor.execute(query, (student_id,))

con.commit()

print("Student deleted successfully!")

cursor.close()
con.close()