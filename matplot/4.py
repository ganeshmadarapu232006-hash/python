import matplotlib.pyplot as plt

transaction = [1200, 2500, 1800, 5000, 3500]

customer = ["Rahul", "Raju", "Ramu", "Rajesh", "Ramesh"]

plt.bar(customer, transaction)

plt.xlabel("Customer")
plt.ylabel("Transaction Amount")
plt.title("Transaction Amount Distribution")

plt.show()