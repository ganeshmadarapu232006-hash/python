try:
    student = {
        "name": "Ganesh",
        "age": 20,
        "branch": "CCN"
    }

    key = input("Enter key: ")

    print("Value =", student[key])

except KeyError:
    print("Error: Key not found in the dictionary.")

except TypeError:
    print("Error: Invalid data type.")