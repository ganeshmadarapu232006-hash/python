f = open("sample.txt", "w")

lines = ["Hello Python\n", "Welcome to File Handling\n", "This is a file"]

f.writelines(lines)

f.close()