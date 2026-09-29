def remove_duplicates(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 5]
result = remove_duplicates(numbers)

print("List without duplicates:", result)