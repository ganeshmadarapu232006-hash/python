try:
    numbers = [10, 20, 30, 40, 50]

    index = int(input("Enter index: "))

    print("Element =", numbers[index])

except IndexError:
    print("Error: Invalid index. Please enter an index from 0 to 4.")

except ValueError:
    print("Error: Please enter a valid number.")