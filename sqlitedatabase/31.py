import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

query = """
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10,2),
    joining_date DATE
)
"""

cursor.execute(query)

print("Employees table created successfully!")

cursor.close()
con.close()