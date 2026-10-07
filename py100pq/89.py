numbers = [0, 1, 0, 3, 12, 0]

result = [i for i in numbers if i != 0]
result += [0] * numbers.count(0)

print(result)