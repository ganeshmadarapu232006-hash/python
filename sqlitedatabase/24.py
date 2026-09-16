import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

student_id = int(input("Enter student ID to delete: "))

query = "DELETE FROM students WHERE id = %s"

cursor.execute(query, (student_id,))

con.commit()

if cursor.rowcount > 0:
    print("Student record deleted successfully!")
else:
    print("Student ID not found!")

cursor.close()
con.close()