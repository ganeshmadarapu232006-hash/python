import json

file = open("employee.json", "r")

data = json.load(file)

file.close()

if isinstance(data, dict):
    employees = [data]
else:
    employees = data

highest_salary = 0
highest_employee = None

for employee in employees:

    salary = int(employee["Salary"])

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = employee

if highest_employee:
    print("Employee with highest salary:")
    print("Employee ID:", highest_employee["Employee ID"])
    print("Name:", highest_employee["Name"])
    print("Department:", highest_employee["Department"])
    print("Job Role:", highest_employee["Job Role"])
    print("Salary:", highest_employee["Salary"])
else:
    print("No employee records found.")