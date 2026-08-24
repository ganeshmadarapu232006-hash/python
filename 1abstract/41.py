from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        print("Company: ABC Technologies")

class Manager(Employee):

    def calculate_salary(self):
        return 60000

class Developer(Employee):

    def calculate_salary(self):
        return 50000

manager = Manager()
developer = Developer()
print("Manager Salary:", manager.calculate_salary())
manager.display_company()

print()

print("Developer Salary:", developer.calculate_salary())
developer.display_company()