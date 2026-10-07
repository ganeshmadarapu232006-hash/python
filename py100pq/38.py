numbers = [10, 20, 10, 30, 10]

value = 10
new_value = 99

i = 0

while i < len(numbers):
    if numbers[i] == value:
        numbers.insert(i + 1, new_value)
        i += 1
    i += 1

print("Updated list:", numbers)