file = open("students.txt", "r")

name = input("Enter student name to search: ")

found = False

for line in file:
    if line.startswith("Name:"):
        student_name = line.strip().split(":")[1].strip()

        if student_name.lower() == name.lower():
            print("Student found:")
            print(line, end="")

            print(next(file), end="")
            print(next(file), end="")
            print(next(file), end="")

            found = True
            break

if not found:
    print("Student not found.")

file.close()