from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        print("employe works")

class Developer(Employee):

    def work(self):
        print("Developer writes and develops software")

class Tester(Employee):

    def work(self):
        print("Tester tests the software and finds bugs")

developer = Developer()
tester = Tester()
developer.work()
tester.work()