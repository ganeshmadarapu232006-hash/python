try:
    balance = float(input("Enter available balance: "))
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Withdrawal amount is greater than available balance.")

    balance = balance - amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)