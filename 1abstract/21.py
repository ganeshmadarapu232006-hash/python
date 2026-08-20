from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass


# Manager class
class Manager(Employee):

    def calculate_salary(self):
        return 60000


# Developer class
class Developer(Employee):

    def calculate_salary(self):
        return 50000


manager = Manager("Ravi", 101)
developer = Developer("Manu", 102)

print("Manager Name:", manager.name)
print("Manager ID:", manager.employee_id)
print("Manager Salary:", manager.calculate_salary())

print()

print("Developer Name:", developer.name)
print("Developer ID:", developer.employee_id)
print("Developer Salary:", developer.calculate_salary())