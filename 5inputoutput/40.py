file = open("sample.txt", "r")
ch = input("Enter the starting character: ")
for line in file:
    if line.startswith(ch):
        print(line, end="")
file.close()