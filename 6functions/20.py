def largest(numbers):
    largest_num = numbers[0]

    for num in numbers:
        if num > largest_num:
            largest_num = num

    return largest_num

numbers = [10, 25, 5, 40, 15]
result = largest(numbers)

print("Largest number:", result)