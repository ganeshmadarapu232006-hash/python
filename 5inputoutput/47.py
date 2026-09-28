file1 = open("sample.txt", "r")

data = file1.read()

file2 = open("lowercase.txt", "w")

file2.write(data.lower())

print("File converted to lowercase successfully.")

file1.close()
