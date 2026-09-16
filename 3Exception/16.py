import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="collegedb"
    )

    print("Database connected successfully!")

except mysql.connector.Error as e:
    print("Error:", e)

finally:
    if 'con' in locals() and con.is_connected():
        con.close()
        print("Database connection closed.")