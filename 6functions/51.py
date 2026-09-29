def min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return (minimum, maximum)

numbers = [10, 25, 5, 40, 15]

result = min_max(numbers)

print("Minimum:", result[0])
print("Maximum:", result[1])