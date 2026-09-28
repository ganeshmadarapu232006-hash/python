with open("sample.txt", "r") as file:
    lines = file.readlines()

for line in lines[-5:]:
    print(line, end="")