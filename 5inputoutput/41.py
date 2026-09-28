file1 = open("numbers.txt", "r")
file2 = open("even.txt", "w")
for num in file1:
    num = int(num)

    if num % 2 == 0:
        file2.write(str(num) + "\n")

print("Even numbers copied successfully.")
file1.close()
file2.close()