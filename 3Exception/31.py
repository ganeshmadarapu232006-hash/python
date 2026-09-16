try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise ValueError("Negative numbers are not allowed.")

    print("You entered:", num)

except ValueError as e:
    print("Error:", e)