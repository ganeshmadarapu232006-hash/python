class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

employee1 = Employee("Ganesh", 101, 25000)

print("Employee Name:", employee1.name)
print("Employee ID:", employee1.employee_id)
print("Employee Salary:", employee1.salary)