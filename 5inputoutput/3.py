# Write five student names into a text file

with open("students.txt", "w") as file:
    file.write("Ganesh\n")
    file.write("Ravi\n")
    file.write("Suresh\n")
    file.write("Priya\n")
    file.write("Anjali\n")

print("Five student names saved successfully.")