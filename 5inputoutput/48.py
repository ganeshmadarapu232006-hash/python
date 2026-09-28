file1 = open("sample.txt", "r")

file2 = open("reverse.txt", "w")

for line in file1:
    reversed_line = line.rstrip("\n")[::-1]

    file2.write(reversed_line + "\n")

print("Each line reversed successfully.")

file1.close()
file2.close()