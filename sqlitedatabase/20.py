import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

query = """
SELECT * FROM students
ORDER BY marks DESC
LIMIT 5
"""

cursor.execute(query)

records = cursor.fetchall()

for student in records:
    print(student)

cursor.close()
con.close()