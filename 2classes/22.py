class Employee:
    company_name = "TCS"   # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company_name)

employee1 = Employee("Ganesh", 30000)
employee2 = Employee("Ravi", 35000)
employee3 = Employee("Kiran", 40000)

employee1.display()
employee2.display()
employee3.display()