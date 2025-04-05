# Hospital Bed Allocation System
# Filename: hospital_bed.py
# Create a `HospitalBed` class with:
# - `bed_number`
# - `patient_name` (default `None`)
# Implement methods:
# - `assign_bed(patient_name)` → Assigns a patient to the bed.
# - `release_bed()` → Frees up the bed

class HospitalBed:
    def __init__(self, bed_number):
        self.bed_number = bed_number
        self.patient_name = None  # Default to no patient assigned

    def assign_bed(self, patient_name):
        if self.patient_name is None:
            self.patient_name = patient_name
            print(f"Bed {self.bed_number} assigned to {patient_name}.")
        else:
            print(f"Bed {self.bed_number} is already occupied by {self.patient_name}.")

    def release_bed(self):
        if self.patient_name is not None:
            released_patient = self.patient_name
            self.patient_name = None
            print(f"Bed {self.bed_number} is now free. Patient {released_patient} has been discharged.")
        else:
            print(f"Bed {self.bed_number} is already free.")