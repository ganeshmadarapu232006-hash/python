file1 = open("sample.txt", "r")
data = file1.read()

file2 = open("uppercase.txt", "w")

file2.write(data.upper())

print("File converted to uppercase successfully.")

file1.close()
file2.close()