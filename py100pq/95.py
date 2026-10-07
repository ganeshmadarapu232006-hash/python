numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maximum = numbers[0]
current = numbers[0]

for i in numbers[1:]:
    current = max(i, current + i)
    maximum = max(maximum, current)

print(maximum)