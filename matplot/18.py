import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [21, 22, 23, 24, 25, 26, 27, 28, 30, 32]
})

plt.hist(
    df["Age"],
    bins=5,
    edgecolor="black"
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()