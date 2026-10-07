def calculate_average(*args):
    total = sum(args)
    average = total / len(args)
    return average

print("Average:", calculate_average(10, 20, 30, 40, 50))