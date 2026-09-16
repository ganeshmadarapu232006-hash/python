try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except TypeError:
    print("Error: Invalid data type.")