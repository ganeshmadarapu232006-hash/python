class InvalidEmailError(Exception):
    pass


try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email address.")

    print("Valid email:", email)

except InvalidEmailError as e:
    print("Error:", e)