numbers = [100, 4, 200, 1, 3, 2]

numbers.sort()

longest = 1
current = 1

for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1] + 1:
        current += 1
        longest = max(longest, current)
    else:
        current = 1

print(longest)