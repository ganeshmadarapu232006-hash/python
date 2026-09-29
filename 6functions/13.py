def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

result = smallest(10, 25, 5)
print("Smallest number:", result)