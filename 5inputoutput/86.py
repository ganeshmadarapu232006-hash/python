import json

employee_id = input("Enter employee ID: ")
name = input("Enter employee name: ")
department = input("Enter department: ")
job_role = input("Enter job role: ")
salary = int(input("Enter salary: "))

employee = {
    "Employee ID": employee_id,
    "Name": name,
    "Department": department,
    "Job Role": job_role,
    "Salary": salary
}
file = open("employee.json", "w")

json.dump(employee, file, indent=4)

file.close()

print("Employee information saved successfully.")