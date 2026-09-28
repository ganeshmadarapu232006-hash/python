filename = input("Enter filename: ")

try:
    file = open(filename, "r")

    data = file.read()

    print("File contents:")
    print(data)

    file.close()

except FileNotFoundError:
    print("File does not exist.")