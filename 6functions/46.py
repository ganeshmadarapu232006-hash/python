def reverse_string(text):
    if text == "":
        return ""
    else:
        return reverse_string(text[1:]) + text[0]


result = reverse_string("Python")
print("Reversed string:", result)