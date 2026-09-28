file = open("sample.txt", "r")

data = file.read()

count = len(data)

print("Total number of characters:", count)

file.close()