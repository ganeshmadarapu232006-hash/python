numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for i in numbers:
    if numbers.count(i) == 1:
        unique.append(i)

print(unique)