import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college_db"
)

cursor = con.cursor()

while True:
    print("\n===== STUDENT DATABASE =====")
    print("1. Insert Student")
    print("2. Display Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # INSERT
    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))

        query = """
        INSERT INTO students (name, age, course, marks)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, age, course, marks)
        cursor.execute(query, values)
        con.commit()

        print("Student inserted successfully!")

    # DISPLAY
    elif choice == 2:
        cursor.execute("SELECT * FROM students")

        records = cursor.fetchall()

        print("\nStudent Records:")
        for student in records:
            print(student)

    # UPDATE
    elif choice == 3:
        student_id = int(input("Enter student ID: "))
        marks = int(input("Enter new marks: "))

        query = "UPDATE students SET marks = %s WHERE id = %s"

        cursor.execute(query, (marks, student_id))
        con.commit()

        if cursor.rowcount > 0:
            print("Marks updated successfully!")
        else:
            print("Student ID not found!")

    # DELETE
    elif choice == 4:
        student_id = int(input("Enter student ID: "))

        query = "DELETE FROM students WHERE id = %s"

        cursor.execute(query, (student_id,))
        con.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student ID not found!")

    # SEARCH
    elif choice == 5:
        student_id = int(input("Enter student ID: "))

        query = "SELECT * FROM students WHERE id = %s"

        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        if student:
            print("\nStudent Details:")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Marks:", student[4])
        else:
            print("Student not found!")

    # EXIT
    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")

cursor.close()
con.close()