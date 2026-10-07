import matplotlib.pyplot as plt

waiting_time = [15, 25, 10, 35, 20]

customer = ["Table1", "Table2", "Table3", "Table4", "Table5"]

plt.bar(customer, waiting_time)

plt.xlabel("Table")
plt.ylabel("Waiting Time (minutes)")
plt.title("Delivery / Waiting Time Distribution")

plt.show()