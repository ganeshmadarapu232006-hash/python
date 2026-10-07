numbers = [1, 2, 2, 3, 3, 3, 4]

least = numbers[0]

for i in numbers:
    if numbers.count(i) < numbers.count(least):
        least = i

print(least)