from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_details(self):
        print("Manager Name:", self.name)
        print("Manager Salary:", self.calculate_salary())


class Developer(Employee):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display_details(self):
        print("Developer Name:", self.name)
        print("Developer Salary:", self.calculate_salary())

manager = Manager("Ravi", 60000)
developer = Developer("Manu", 50000)

manager.display_details()
print()

developer.display_details()