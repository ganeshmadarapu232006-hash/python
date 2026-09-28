f = open("sample.txt", "r")

print(f.tell())

data = f.read(5)

print(data)
print(f.tell())

f.close()