try:
    string = input("Enter a number: ")
    number = int(string)

    print("Integer value:", number)

except ValueError:
    print("Error: Please enter a valid integer.")