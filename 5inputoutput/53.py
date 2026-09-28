file = open("numbers.txt", "r")
largest = int(file.readline())

for num in file:
    num = int(num)

    if num > largest:
        largest = num

print("Largest number =", largest)

file.close()