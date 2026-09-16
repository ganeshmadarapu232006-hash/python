class InvalidUsernameError(Exception):
    pass


try:
    username = input("Enter username: ")

    if username == "":
        raise InvalidUsernameError("Username cannot be empty.")

    print("Valid username:", username)

except InvalidUsernameError as e:
    print("Error:", e)