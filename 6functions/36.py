def employee_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee_info(
    name="Ganesh",
    employee_id=101,
    department="IT",
    salary=25000
)