def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    return unique_numbers[-2]

numbers = [10, 20, 5, 40, 30]
result = second_largest(numbers)

print("Second largest number:", result)