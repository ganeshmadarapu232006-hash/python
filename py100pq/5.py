numbers = [25, 10, 45, 5, 30]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number:", smallest)