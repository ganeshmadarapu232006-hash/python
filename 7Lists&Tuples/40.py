def separate_even_odd(*args):
    even = []
    odd = []

    for num in args:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd


even, odd = separate_even_odd(10, 15, 20, 25, 30, 35)

print("Even Numbers:", even)
print("Odd Numbers:", odd)