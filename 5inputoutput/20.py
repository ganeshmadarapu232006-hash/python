with open("sample.txt", "w") as file:
    file.write("Welcome to Python\n")
    file.write("This is the original data.\n")

with open("sample.txt", "r") as file:
    print("Original contents:")
    print(file.read())

with open("sample.txt", "a") as file:
    file.write("This is the new appended data.\n")

with open("sample.txt", "r") as file:
    print("After appending:")
    print(file.read())