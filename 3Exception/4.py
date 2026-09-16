student = {
    "name": "Ganesh",
    "age": 20,
    "course": "Diploma"
}

try:
    key = input("Enter the key: ")
    print("Value:", student[key])

except KeyError:
    print("Error: Key not found in the dictionary.")