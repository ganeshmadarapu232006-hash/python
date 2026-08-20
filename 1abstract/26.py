from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):

    def display_details(self):
        print("Manager Name:", self.name)
        print("Manager Salary:", self.salary)

class Developer(Employee):

    def display_details(self):
        print("Developer Name:", self.name)
        print("Developer Salary:", self.salary)

class Tester(Employee):

    def display_details(self):
        print("Tester Name:", self.name)
        print("Tester Salary:", self.salary)

manager = Manager("Ravi", 60000)
developer = Developer("Manu", 50000)
tester = Tester("Suresh", 40000)

manager.display_details()

print()

developer.display_details()

print()

tester.display_details()