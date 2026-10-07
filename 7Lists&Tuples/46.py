def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:]) + text[0]


print("Reversed:", reverse_string("Python"))