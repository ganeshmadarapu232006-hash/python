def student_details(*args, **kwargs):
    print("Student Details:")

    for value in args:
        print(value)

    print("Marks:")

    for subject, marks in kwargs.items():
        print(subject, ":", marks)


student_details(
    "Ganesh",
    20,
    "Computer & Communication Networking",
    Math=85,
    Python=90,
    Java=80
)