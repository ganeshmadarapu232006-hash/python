try:
    file = open("student.txt", "r")

    data = file.read()
    print("File content:")
    print(data)

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied. You cannot access this file.")