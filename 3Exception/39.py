try:
    attendance = float(input("Enter student's attendance percentage: "))

    required = 75

    if attendance < required:
        raise ValueError("Attendance is below the required 75%.")

    print("Attendance is sufficient.")

except ValueError as e:
    print("Error:", e)