try:
    file = open("numbers.txt", "r")

    for line in file:
        try:
            number = int(line.strip())
            print("Number =", number)

        except ValueError:
            print("Invalid data:", line.strip())

    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")