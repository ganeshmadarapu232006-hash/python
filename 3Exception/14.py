try:
    num = int(input("Enter a number: "))
    
except ValueError:
    print("Please enter a valid number")

else:
    square = num * num
    print("Square:", square)