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
WHERE marks BETWEEN %s AND %s
"""

values = (50, 80)

cursor.execute(query, values)

records = cursor.fetchall()

for student in records:
    print(student)

cursor.close()
con.close()