file = open("sample.txt", "r")
word = input("Enter the word to search: ")
for line in file:
    if word in line:
        print(line, end="")
file.close()