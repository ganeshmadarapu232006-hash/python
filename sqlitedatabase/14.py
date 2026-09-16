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
SET course = %s
WHERE id = %s
"""

values = ("Java", 1)

cursor.execute(query, values)

con.commit()

print("Student course updated successfully!")

cursor.close()
con.close()