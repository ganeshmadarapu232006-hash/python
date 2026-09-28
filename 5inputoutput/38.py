file = open("sample.txt", "r")
data = file.read()
uppercase = 0
lowercase = 0
for ch in data:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Total uppercase characters:", uppercase)
print("Total lowercase characters:", lowercase)
file.close()