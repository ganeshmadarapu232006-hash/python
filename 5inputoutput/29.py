f = open("sample.txt", "r")

print("Initial position:", f.tell())

f.read(5)
print("After reading 5 characters:", f.tell())

f.seek(0)
print("After seek(0):", f.tell())

f.seek(6)
print("After seek(6):", f.tell())

f.close()