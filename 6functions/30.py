def largest_smallest(numbers):
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    return largest, smallest


numbers = [10, 25, 5, 40, 15]
largest, smallest = largest_smallest(numbers)

print("Largest:", largest)
print("Smallest:", smallest)