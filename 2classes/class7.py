class College:
    def __init__(self, college_name, location, course):
        self.college_name = college_name
        self.location = location
        self.course = course


# Create three objects
college1 = College("Aditya Polytechnic College", "Surampalem", "CCN")
college2 = College("ABC Polytechnic College", "Rajahmundry", "CSE")
college3 = College("XYZ Polytechnic College", "Kakinada", "ECE")


# Display details
print("College 1:")
print("Name:", college1.college_name)
print("Location:", college1.location)
print("Course:", college1.course)

print("\nCollege 2:")
print("Name:", college2.college_name)
print("Location:", college2.location)
print("Course:", college2.course)

print("\nCollege 3:")
print("Name:", college3.college_name)
print("Location:", college3.location)
print("Course:", college3.course)