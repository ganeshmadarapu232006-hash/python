try:
    numbers = [10, 20, 30, 40, 50]

    index = int(input("Enter list index: "))

    print("Element =", numbers[index])

except ValueError:
    print("Error: Please enter a valid integer.")

except IndexError:
    print("Error: Index is out of range.")

except TypeError:
    print("Error: Invalid data type.")

except Exception as e:
    print("Error:", e)