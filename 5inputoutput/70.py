file = open("students.txt", "r")

lines = file.readlines()
file.close()

print("Students who scored above 75 marks:")
print("----------------------------------")

for i in range(len(lines)):
    if lines[i].strip().startswith("Marks:"):
        marks = int(lines[i].split(":")[1].strip())

        if marks > 75:
            print(lines[i - 3], end="")
            print(lines[i - 2], end="")
            print(lines[i - 1], end="")
            print(lines[i], end="")
            print("--------------------")
