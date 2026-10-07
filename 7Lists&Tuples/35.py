def find_largest(*args):
    largest = args[0]

    for num in args:
        if num > largest:
            largest = num

    return largest

print("Largest Number:", find_largest(10, 25, 5, 40, 15))