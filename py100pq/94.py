numbers = [10, 22, 9, 33, 21, 50, 41, 60]

result = []

for i in numbers:
    if not result or i > result[-1]:
        result.append(i)

print(result)