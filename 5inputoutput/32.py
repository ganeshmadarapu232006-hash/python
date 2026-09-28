file = open("sample.txt", "r")

data = file.read()

words = data.split()

count = len(words)

print("Total number of words:", count)

file.close()