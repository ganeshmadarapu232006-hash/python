file = open("numbers.txt", "r")

total = 0
count = 0

for num in file:
    total += int(num)
    count += 1

average = total / count

print("Average =", average)

file.close()