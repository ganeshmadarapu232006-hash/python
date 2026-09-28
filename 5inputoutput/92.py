try:
    file = open("data.txt", "r")

    data = file.read()
    print(data)

    file.close()

except PermissionError:
    print("Permission denied. You do not have permission to access this file.")