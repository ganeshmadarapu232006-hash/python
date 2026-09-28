f = open("sample.txt", "r")

f.seek(6)

data = f.read()

print(data)

f.close()