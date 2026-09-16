import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

query = """
INSERT INTO students (name, age, course, marks)
VALUES (%s, %s, %s, %s)
"""

values = ("Suresh", 21, "Python", 82)

cursor.execute(query, values)

con.commit()

print("New student inserted successfully!")

cursor.close()
con.close()