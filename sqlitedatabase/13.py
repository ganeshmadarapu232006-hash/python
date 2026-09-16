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
SET marks = %s
WHERE id = %s
"""

values = (95, 1)

cursor.execute(query, values)

con.commit()

print("Student marks updated successfully!")

cursor.close()
con.close()