def student_details(*args, **kwargs):
    print("Student Details:")

    for value in args:
        print("Subject:", value)

    print("\nStudent Information:")
    for key, value in kwargs.items():
        print(key, ":", value)


student_details(
    "Maths", "Physics", "Computer Science",
    name="Ganesh",
    age=20,
    marks=85
)