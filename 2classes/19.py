class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Experience:", self.experience, "years")

teacher1 = Teacher("Ravi", "Python", 3)
teacher2 = Teacher("Sita", "Java", 5)
teacher3 = Teacher("Kiran", "SQL", 2)

teacher1.display()
teacher2.display()
teacher3.display()