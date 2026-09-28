file = open("sample.txt", "r")
data = file.read()
count = 0

for ch in data:
    if ch == " ":
        count += 1

print("Total number of spaces:", count)
file.close()