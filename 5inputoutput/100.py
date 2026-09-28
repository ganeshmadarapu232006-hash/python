try:
    source = input("Enter source filename: ")
    destination = input("Enter destination filename: ")

    file1 = open(source, "r")

    data = file1.read()

    file1.close()

    file2 = open(destination, "w")

    
    file2.write(data)

    file2.close()

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")

except PermissionError:
    print("Permission denied.")

except Exception as e:
    print("Error:", e)