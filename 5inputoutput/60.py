file1 = open("numbers.txt", "r")

numbers = []

for num in file1:
    numbers.append(int(num))

numbers.sort()

file2 = open("sorted.txt", "w")

for num in numbers:
    file2.write(str(num) + "\n")

print("Numbers sorted successfully.")

file1.close()
file2.close()