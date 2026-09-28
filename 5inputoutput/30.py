with open("example.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("Welcome to File Handling")

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)