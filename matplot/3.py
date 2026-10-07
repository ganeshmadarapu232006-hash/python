import matplotlib.pyplot as plt

marks = [35, 42, 45, 48, 50, 52, 55, 58, 60, 62]

student = ["rahul", "raju", "ramu", "rajesh", "ramesh",
           "rajesh", "raj", "rambabu", "rani", "renuka"]

plt.bar(student, marks)

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Marks of Students")

plt.show()