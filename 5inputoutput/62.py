file = open("students.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    marks = input("Enter marks: ")

    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Course: " + course + "\n")
    file.write("Marks: " + marks + "\n")
    file.write("--------------------\n")

print("Student records saved successfully.")

file.close()