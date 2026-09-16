import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")
marks = int(input("Enter student marks: "))

query = """
INSERT INTO students (name, age, course, marks)
VALUES (%s, %s, %s, %s)
"""

values = (name, age, course, marks)

cursor.execute(query, values)

con.commit()

print("Student details inserted successfully!")

cursor.close()
con.close()