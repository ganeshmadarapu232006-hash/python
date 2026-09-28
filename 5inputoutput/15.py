import os

filename = "sample.txt"

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File does not exist.")