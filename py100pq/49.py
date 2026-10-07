def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Ganesh", age=20, course="CCN")