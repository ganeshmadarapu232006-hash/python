def find_topper(marks):
    topper = max(marks, key=marks.get)
    return topper

student_marks = {
    "Ganesh": 85,
    "Ravi": 92,
    "Suresh": 78,
    "Kiran": 88
}

print("Topper:", find_topper(student_marks))