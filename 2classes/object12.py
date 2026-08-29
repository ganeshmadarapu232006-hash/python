class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employee1 = Employee("Ganesh", "IT", 30000)
employee2 = Employee("Rahul", "HR", 35000)
employee3 = Employee("Kiran", "Finance", 40000)
employee4 = Employee("Arjun", "Marketing", 32000)
employee5 = Employee("Suresh", "IT", 45000)

print("Employee 1:", employee1.name, employee1.department, employee1.salary)
print("Employee 2:", employee2.name, employee2.department, employee2.salary)
print("Employee 3:", employee3.name, employee3.department, employee3.salary)
print("Employee 4:", employee4.name, employee4.department, employee4.salary)
print("Employee 5:", employee5.name, employee5.department, employee5.salary)