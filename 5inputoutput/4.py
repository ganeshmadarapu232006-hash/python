# Write five numbers into a text file

with open("numbers.txt", "w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("30\n")
    file.write("40\n")
    file.write("50\n")

print("Five numbers saved successfully.")