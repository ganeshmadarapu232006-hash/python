from abc import ABC, abstractmethod

# Abstract class
class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self):
        pass


# PDFReport class
class PDFReport(Report):

    def generate(self):
        print("PDF report generated")

    def export(self):
        print("PDF report exported")


# ExcelReport class
class ExcelReport(Report):

    def generate(self):
        print("Excel report generated")

    def export(self):
        print("Excel report exported")


# Creating objects
pdf = PDFReport()
excel = ExcelReport()

# Calling methods
pdf.generate()
pdf.export()

print()

excel.generate()
excel.export()