import matplotlib.pyplot as plt

salary = [15000, 16000, 17000, 18000, 19000,
          21000, 22000, 23000, 24000, 25000,
          26000, 27000, 28000, 29000, 30000]

bins = [10000, 15000, 20000, 25000, 30000, 35000]

plt.hist(salary, bins=bins)

plt.xlabel("Salary")
plt.ylabel("Frequency (Number of Employees)")
plt.title("Employee Salary Distribution")

plt.show()