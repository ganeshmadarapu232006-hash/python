file1 = open("numbers.txt", "r")

file2 = open("cubes.txt", "w")

for num in file1:
    num = int(num)
    cube = num * num * num

    file2.write(str(cube) + "\n")

print("Cubes created successfully.")

file1.close()
file2.close()