file1 = open("sample.txt", "r")

lines = file1.readlines()

file2 = open("unique.txt", "w")

seen = set()

for line in lines:
    if line not in seen:
        file2.write(line)
        seen.add(line)

print("Duplicate lines removed successfully.")

file1.close()
file2.close()