numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

best = []
maximum = numbers[0]

for i in range(len(numbers)):
    total = 0

    for j in range(i, len(numbers)):
        total += numbers[j]

        if total > maximum:
            maximum = total
            best = numbers[i:j + 1]

print(best)
print(maximum)