file = open("students.txt", "r")

lines = file.readlines()
file.close()

student_id = input("Enter student ID to delete: ")

new_lines = []
i = 0
found = False

while i < len(lines):
    if lines[i].startswith("ID:"):
        id_value = lines[i].strip().split(":")[1].strip()

        if id_value == student_id:
            i += 6
            found = True
        else:
            new_lines.extend(lines[i:i + 6])
            i += 6
    else:
        i += 1

file = open("students.txt", "w")
file.writelines(new_lines)
file.close()

if found:
    print("Student record deleted successfully.")
else:
    print("Student ID not found.")