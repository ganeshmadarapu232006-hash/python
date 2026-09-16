import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

query = """
UPDATE students
SET name = %s
WHERE id = %s
"""

values = ("Suresh", 1)

cursor.execute(query, values)

con.commit()

print("Student name updated successfully!")

cursor.close()
con.close()