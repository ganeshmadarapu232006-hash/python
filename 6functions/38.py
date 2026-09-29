def average(*args):
    total = 0

    for num in args:
        total += num

    return total / len(args)

result = average(10, 20, 30, 40, 50)
print("Average:", result)