import json

name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

product = {
    "Product Name": name,
    "Price": price,
    "Quantity": quantity
}

file = open("product.json", "w")

json.dump(product, file, indent=4)

file.close()

print("Product information saved successfully.")