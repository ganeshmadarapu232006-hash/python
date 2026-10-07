import matplotlib.pyplot as plt

ages = [
    18, 19, 20, 21, 22,
    23, 24, 25, 26, 27,
    28, 29, 30, 31, 32,
    33, 35, 36, 40
]

plt.hist(
    ages,
    bins=10,
    density=True,
    edgecolor="black"
)

plt.title("Age Distribution - Density Histogram")
plt.xlabel("Age")
plt.ylabel("Density")

plt.show()