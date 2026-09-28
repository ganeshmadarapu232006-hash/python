file1 = open("sample.txt", "r")

lines = file1.readlines()

file2 = open("reverse.txt", "w")

for line in reversed(lines):
    file2.write(line)

print("File contents written in reverse order successfully.")

file1.close()
file2.close()