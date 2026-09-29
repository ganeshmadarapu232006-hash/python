def number_squares(numbers):
    result = {}

    for num in numbers:
        result[num] = num ** 2

    return result

numbers = [2, 3, 4, 5]

result = number_squares(numbers)

print(result)