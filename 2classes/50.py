class HospitalPatient:
    def __init__(self, name, age, disease, patient_id):
        self.name = name
        self.age = age
        self.disease = disease
        self.patient_id = patient_id

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Patient Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)

patient1 = HospitalPatient(101, 25, "Fever", "P001")

patient1.display()