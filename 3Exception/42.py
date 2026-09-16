class InsufficientBalanceError(Exception):
    pass


try:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")

    balance = balance - amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print("Error:", e)