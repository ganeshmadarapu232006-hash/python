import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

product_id = int(input("Enter product ID: "))

query = "SELECT * FROM products WHERE id = %s"

cursor.execute(query, (product_id,))

product = cursor.fetchone()

if product:
    print("\nProduct Information")
    print("ID:", product[0])
    print("Name:", product[1])
    print("Price:", product[2])
    print("Quantity:", product[3])
else:
    print("Product not found!")

cursor.close()
con.close()