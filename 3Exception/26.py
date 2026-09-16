try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("Result =", a + b)

    elif operation == "-":
        print("Result =", a - b)

    elif operation == "*":
        print("Result =", a * b)

    elif operation == "/":
        print("Result =", a / b)

    else:
        print("Error: Invalid operation.")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except TypeError:
    print("Error: Invalid data type.")