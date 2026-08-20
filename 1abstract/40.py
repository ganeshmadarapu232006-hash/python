from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):

    def generate(self):
        print("Generating PDF Report")

class ExcelReport(Report):

    def generate(self):
        print("Generating Excel Report")

class HTMLReport(Report):

    def generate(self):
        print("Generating HTML Report")

reports = [
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]

for report in reports:
    report.generate()