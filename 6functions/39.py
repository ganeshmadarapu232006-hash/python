def profile(**kwargs):
    print("Person Profile:")

    for key, value in kwargs.items():
        print(key, ":", value)


profile(
    name="Ganesh",
    age=20,
    city="Rajahmundry",
    profession="Student"
)