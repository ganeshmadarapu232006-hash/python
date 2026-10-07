def create_profile(**kwargs):
    print("Person's Profile:")

    for key, value in kwargs.items():
        print(key, ":", value)


create_profile(
    name="Ganesh",
    age=20,
    city="Rajahmundry",
    profession="Web Developer"
)