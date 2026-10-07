import matplotlib.pyplot as plt

price = [500, 800, 1200, 1500, 2000]

product = ["Table1", "Table2", "Table3", "Table4", "Table5"]

plt.bar(product, price)

plt.xlabel("Product")
plt.ylabel("Price")
plt.title("Product Price Distribution")

plt.show()