def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b
    division = a / b

    return total, difference, product, division


result = calculate(20, 5)

print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Division:", result[3])