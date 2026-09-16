try:
    file = open("sample.txt", "r")
    
except FileNotFoundError:
    print("File not found")

else:
    print("File contents:")
    print(file.read())
    file.close()

finally:
    print("Program execution completed")