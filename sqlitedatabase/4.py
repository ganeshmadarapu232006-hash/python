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

values = [
    ("Ganesh", 20, "Python", 85),
    ("Ravi", 21, "Java", 78),
    ("Manoj", 20, "Python", 90),
    ("Kiran", 22, "HTML", 88),
    ("Arun", 21, "JavaScript", 75)
]

cursor.executemany(query, values)

con.commit()

print("Five student records inserted successfully!")

cursor.close()
con.close()