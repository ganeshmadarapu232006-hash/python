with open("sample.txt", "r") as file:
    for i in range(5):
        line = file.readline()
        if line == "":
            break
        print(line, end="")