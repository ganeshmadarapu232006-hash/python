class InsufficientStockError(Exception):
    pass


try:
    stock = int(input("Enter available stock: "))
    quantity = int(input("Enter required quantity: "))

    if quantity > stock:
        raise InsufficientStockError("Insufficient stock available.")

    stock = stock - quantity

    print("Product sold successfully.")
    print("Remaining stock:", stock)

except InsufficientStockError as e:
    print("Error:", e)