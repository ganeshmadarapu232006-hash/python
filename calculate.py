# Calculator using Operators in Python

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Calculator ---")

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** num2)
print("\n--- Comparison ---")
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("\n--- Logical Operators ---")
print("Both numbers are positive:", num1 > 0 and num2 > 0)
print("At least one is positive:", num1 > 0 or num2 > 0)
print("num1 is not zero:", not num1 == 0)