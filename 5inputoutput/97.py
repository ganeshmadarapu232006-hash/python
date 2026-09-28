import json

try:
    file = open("student.json", "r")

    data = json.load(file)

    file.close()

    print("JSON data:")
    print(data)

except FileNotFoundError:
    print("JSON file not found.")

except json.JSONDecodeError:
    print("Invalid JSON data.")

except Exception as e:
    print("Error:", e)