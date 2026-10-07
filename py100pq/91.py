numbers = [1, 4, 3, 8, 5, 6, 2]

even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]

result = even + odd

print(result)