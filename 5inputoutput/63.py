file = open("students.txt", "r")

data = file.read()

print("Student Records:")
print(data)

file.close()