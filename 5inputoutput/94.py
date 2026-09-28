import os

filename = "data.txt"

if os.path.exists(filename):
    file = open(filename, "r")

    data = file.read()
    print(data)

    file.close()
else:
    print("File does not exist.")