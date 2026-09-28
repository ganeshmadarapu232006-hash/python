file1 = open("numbers.txt", "r")

even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")

for num in file1:
    num = int(num)

    if num % 2 == 0:
        even_file.write(str(num) + "\n")
    else:
        odd_file.write(str(num) + "\n")

print("Even and odd numbers separated successfully.")

file1.close()
even_file.close()
odd_file.close()