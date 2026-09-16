try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Eligible: Age is 18 or above.")

except ValueError as e:
    print("Error:", e)