from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        print("Report Information: Monthly Sales Report")

class SalesReport(Report):

    def generate(self):
        print("Generating Sales Report...")

report = SalesReport()
report.generate()
report.display_report_info()