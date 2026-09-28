import json

file = open("product.json", "r")

product = json.load(file)

file.close()

total = product["Price"] * product["Quantity"]

print("Product Name:", product["Product Name"])
print("Price:", product["Price"])
print("Quantity:", product["Quantity"])
print("Total Inventory Value:", total)