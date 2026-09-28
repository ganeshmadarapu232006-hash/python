file = open("students.txt", "r")

student_ID = input("Enter student ID to search: ")

found = False

for line in file:
    if line.startswith("ID:"):
        id_value = line.strip().split(":")[1].strip()

        if id_value == student_ID:
            print("Student found:")
            print(line, end="")
            print(next(file), end="")
            print(next(file), end="")
            print(next(file), end="")
            print(next(file), end="")

            found = True
            break

if not found:
    print("Student not found.")

file.close()