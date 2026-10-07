def total_price(price, tax=18):
    return price + (price * tax / 100)

print(total_price(1000))