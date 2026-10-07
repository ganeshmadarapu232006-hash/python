import matplotlib.pyplot as plt

age = [18, 21, 22, 25, 27, 28, 30, 31, 32, 35,
       36, 38, 40, 41, 42, 45, 47, 50, 52, 55,
       23, 24, 26, 29, 33, 34, 37, 39, 43, 48]

plt.hist(age)

plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.title("Age Distribution of Customers")

plt.show()