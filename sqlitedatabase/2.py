import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

if con.is_connected():
    print("MySQL connection successful!")

con.close()