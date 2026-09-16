try:
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance")

    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)

finally:
    print("Thank you for using the bank service")