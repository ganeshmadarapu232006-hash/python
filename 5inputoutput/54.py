file = open("numbers.txt", "r")

smallest = int(file.readline())

for num in file:
    num = int(num)

    if num < smallest:
        smallest = num

print("Smallest number =", smallest)

file.close()