try:
    student = {
        "name": "Ganesh",
        "age": 20,
        "branch": "CCN"
    }

    key = input("Enter dictionary key: ")

    if not key:
        raise ValueError("Input cannot be empty.")

    print("Value =", student[key])

except ValueError as e:
    print("Error:", e)

except KeyError:
    print("Error: Key not found in the dictionary.")