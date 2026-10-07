def calculate_sum(*args):
    total = 0

    for x in args:
        total += x

    return total

print(calculate_sum(10, 20, 30, 40))