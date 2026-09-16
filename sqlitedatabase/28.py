import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

name = input("Enter employee name: ")
department = input("Enter department: ")
salary = float(input("Enter salary: "))

query = """
INSERT INTO employees (name, department, salary)
VALUES (%s, %s, %s)
"""

values = (name, department, salary)

cursor.execute(query, values)

con.commit()

print("Employee details inserted successfully!")

cursor.close()
con.close()