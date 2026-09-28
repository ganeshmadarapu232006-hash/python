with open("sample.txt", "r") as file:
    while True:
        char = file.read(1)

        if char == "":
            break

        print(char)