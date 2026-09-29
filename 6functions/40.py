def separate_even_odd(*args):
    even = []
    odd = []

    for num in args:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd


even, odd = separate_even_odd(1, 2, 3, 4, 5, 6, 7, 8)

print("Even numbers:", even)
print("Odd numbers:", odd)