numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)