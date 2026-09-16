try:
    file = open("student.txt", "r")
    
    data = file.read()
    print("File content:")
    print(data)
    
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")