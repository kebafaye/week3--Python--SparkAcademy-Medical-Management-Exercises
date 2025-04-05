# Pharmacy Prescription System
# Filename: prescription.py
# Create a `Prescription` class with:
# - `patient_name`
# - `medications` (dictionary with drug names as keys and dosages as values)
# Implement methods:
# - `add_medication(drug, dosage)` → Adds a drug and dosage.
# - `view_prescription()` → Displays all prescribed medications.

class Prescription:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.medications = {}  # Dictionary to store medications and dosages

    def add_medication(self, drug, dosage):
        self.medications[drug] = dosage
        print(f"Added {drug} ({dosage}) to {self.patient_name}'s prescription.")

    def view_prescription(self):
        if self.medications:
            print(f"Prescription for {self.patient_name}:")
            for drug, dosage in self.medications.items():
                print(f"- {drug}: {dosage}")
        else:
            print(f"No medications prescribed for {self.patient_name}.")