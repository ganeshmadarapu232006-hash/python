class InvalidTransactionError(Exception):
    pass


try:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter transaction amount: "))

    if amount <= 0:
        raise InvalidTransactionError("Transaction amount must be greater than zero.")

    if amount > balance:
        raise InvalidTransactionError("Insufficient balance for this transaction.")

    balance = balance - amount

    print("Transaction successful.")
    print("Remaining balance:", balance)

except InvalidTransactionError as e:
    print("Error:", e)