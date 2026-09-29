def keys_greater_than_50(data):
    result = []
    
    for key, value in data.items():
        if value > 50:
            result.append(key)
    
    return result

marks = {
    "Ganesh": 45,
    "Ravi": 75,
    "Suresh": 60,
    "Kiran": 40
}

print("Keys with values greater than 50:", keys_greater_than_50(marks))