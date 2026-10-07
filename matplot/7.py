import matplotlib.pyplot as plt

purchase = [2, 5, 3, 7, 4]

customer = ["Table1", "Table2", "Table3", "Table4", "Table5"]

plt.bar(customer, purchase)

plt.xlabel("Customer")
plt.ylabel("Number of Purchases")
plt.title("Customer Purchase Frequency")

plt.show()