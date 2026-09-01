class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

employee1 = Employee(101, "Ganesh", "IT", 30000)

print("Employee ID:", employee1.employee_id)
print("Name:", employee1.name)
print("Department:", employee1.department)
print("Salary:", employee1.salary)