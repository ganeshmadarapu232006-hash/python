def even_numbers(numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = even_numbers(numbers)

print("Even numbers:", result)