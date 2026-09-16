try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)

    try:
        print("Division =", a / b)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")