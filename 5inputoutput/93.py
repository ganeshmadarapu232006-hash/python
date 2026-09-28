file = None

try:
    file = open("data.txt", "r")

    data = file.read()
    print(data)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    if file is not None:
        file.close()

    print("File operation completed.")