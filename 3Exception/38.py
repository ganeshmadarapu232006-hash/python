try:
    num = int(input("Enter a number: "))

    if num <= 0:
        raise ValueError("Number must be positive.")

    print("Valid positive number:", num)

except ValueError as e:
    print("Error:", e)