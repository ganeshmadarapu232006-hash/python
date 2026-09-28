file = open("numbers.txt", "r")

positive = 0
negative = 0
zero = 0

for num in file:
    num = int(num)

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zero values:", zero)

file.close()