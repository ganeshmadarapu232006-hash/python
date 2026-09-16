import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

# Accept details from user
student_id = int(input("Enter student ID: "))
new_marks = int(input("Enter new marks: "))

# Update marks
query = """
UPDATE students
SET marks = %s
WHERE id = %s
"""

values = (new_marks, student_id)

cursor.execute(query, values)

con.commit()

if cursor.rowcount > 0:
    print("Student marks updated successfully!")
else:
    print("Student ID not found!")

cursor.close()
con.close()