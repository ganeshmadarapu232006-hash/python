class InvalidPasswordError(Exception):
    pass


try:
    password = input("Enter your password: ")

    if len(password) < 8:
        raise InvalidPasswordError("Password must contain at least 8 characters.")

    print("Password is valid.")

except InvalidPasswordError as e:
    print("Error:", e)