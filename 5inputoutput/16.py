try:
    with open("sample.txt", "x") as file:
        file.write("Welcome to Python")
    print("File created successfully.")

except FileExistsError:
    print("File already exists.")