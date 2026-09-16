import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

# Accept student name from user
name = input("Enter student name: ")

# Search student
query = "SELECT * FROM students WHERE name = %s"

cursor.execute(query, (name,))

records = cursor.fetchall()

if records:
    print("\nStudent found:")
    for student in records:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Marks:", student[4])
        print("------------------")
else:
    print("Student not found!")

cursor.close()
con.close()