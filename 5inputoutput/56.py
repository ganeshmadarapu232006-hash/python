file1 = open("numbers.txt", "r")

file2 = open("squares.txt", "w")

for num in file1:
    num = int(num)
    square = num * num

    file2.write(str(square) + "\n")

print("Squares created successfully.")

file1.close()
file2.close()