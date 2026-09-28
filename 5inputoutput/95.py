file = open("numbers.txt", "r")

total = 0

for line in file:
    try:
        number = int(line.strip())
        total += number
        print("Valid number:", number)

    except ValueError:
        print("Invalid data:", line.strip())

file.close()

print("Total:", total)