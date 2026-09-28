file = open("sample.txt", "r")

data = file.read()

data = " ".join(data.split())

file = open("sample.txt", "w")

file.write(data)

print("Extra spaces removed successfully.")

file.close()