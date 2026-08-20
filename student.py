# Student details using built-in data types 
name = input("Enter student name: ")
age = int(input("Enter student age: "))
percentage = float(input("Enter percentage: "))
subjects = ["Python", "Java", "MySQL", "HTML"]
college_details = ("Aditya Polytechnic College", "Diploma")
student = {
    "Name": name,
    "Age": age,
    "Percentage": percentage
}
passed = percentage >= 40
print("\n--- Student Details ---")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Percentage:", student["Percentage"])
print("Subjects:", subjects)
print("College:", college_details[0])
print("Course:", college_details[1])
print("Passed:", passed)