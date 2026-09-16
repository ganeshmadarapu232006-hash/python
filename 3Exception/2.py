try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("First number:", num1)
    print("Second number:", num2)

except ValueError:
    print("Invalid input! Please enter numbers only.")