class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

employee1 = Employee("Ganesh", 30000)

print("Employee Name:", employee1.name)
print("Monthly Salary:", employee1.monthly_salary)
print("Annual Salary:", employee1.annual_salary())