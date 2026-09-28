file = open("numbers.txt", "r")

numbers = []
duplicates = []

for num in file:
    num = int(num)

    if num in numbers:
        if num not in duplicates:
            duplicates.append(num)
    else:
        numbers.append(num)

print("Duplicate numbers:", duplicates)

file.close()