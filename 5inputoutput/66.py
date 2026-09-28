file = open("students.txt", "r")

lines = file.readlines()
file.close()

student_id = input("Enter student ID: ")
new_marks = input("Enter new marks: ")

found = False

for i in range(len(lines)):
    if lines[i].startswith("ID:"):
        id_value = lines[i].strip().split(":")[1].strip()

        if id_value == student_id:
            lines[i + 3] = "Marks: " + new_marks + "\n"
            found = True
            break

file = open("students.txt", "w")
file.writelines(lines)
file.close()

if found:
    print("Marks updated successfully.")
else:
    print("Student ID not found.")