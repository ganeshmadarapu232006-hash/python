import matplotlib.pyplot as plt

employee = ["Raju", "Rahul", "Siva", "Vijay"]

salary = [15000, 17000, 18000, 19000]

plt.bar(employee, salary)

plt.xlabel("Employee")
plt.ylabel("Salary")

plt.title("Employee Salaries")

plt.show()