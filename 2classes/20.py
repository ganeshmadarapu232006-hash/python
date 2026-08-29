class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

    def display(self):
        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Doctor Name:", self.doctor_name)

patient1 = Hospital("Ravi", 25, "Fever", "Dr. Kumar")
patient2 = Hospital("Sita", 30, "Diabetes", "Dr. Priya")
patient3 = Hospital("Rahul", 40, "Cold", "Dr. Anil")

patient1.display()
patient2.display()
patient3.display()