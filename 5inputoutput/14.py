with open("sample.txt", "w") as file:
    file.write("Original content\n")

with open("sample.txt", "r") as file:
    print("Using r mode:")
    print(file.read())

with open("sample.txt", "a") as file:
    file.write("New content added\n")

with open("sample.txt", "r") as file:
    print("After using a mode:")
    print(file.read())