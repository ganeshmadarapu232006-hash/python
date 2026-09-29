def largest(*args):
    largest_num = args[0]

    for num in args:
        if num > largest_num:
            largest_num = num

    return largest_num

result = largest(10, 25, 5, 40, 15)
print("Largest number:", result)