def total_price(price, tax=18):
    tax_amount = price * tax / 100
    total = price + tax_amount
    return total

result = total_price(1000)
print("Total Price:", result)