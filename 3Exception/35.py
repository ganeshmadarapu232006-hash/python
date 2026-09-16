try:
    quantity = int(input("Enter product quantity: "))

    if quantity <= 0:
        raise ValueError("Product quantity must be greater than zero.")

    print("Valid quantity:", quantity)

except ValueError as e:
    print("Error:", e)