class Employee:
    company_name = "ABC Company"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

employee1 = Employee("Ganesh")
employee2 = Employee("Ravi")
employee3 = Employee("Manoj")

print("Company Name:", Employee.company_name)
print("Employee 1:", employee1.name)
print("Employee 2:", employee2.name)
print("Employee 3:", employee3.name)
print("Total Employees:", Employee.employee_count)