def count_even_odd(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return {"even": even, "odd": odd}

numbers = [10, 15, 20, 25, 30, 35]

result = count_even_odd(numbers)

print(result)