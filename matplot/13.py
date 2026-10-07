import matplotlib.pyplot as plt

ages = [22, 25, 28, 30, 32, 35, 36, 38, 40, 42,
        45, 47, 50, 52, 55, 58, 60, 62, 65, 68]

plt.hist(
    ages,
    bins=10,
    edgecolor="black",
    alpha=0.7
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis="y")

plt.show()