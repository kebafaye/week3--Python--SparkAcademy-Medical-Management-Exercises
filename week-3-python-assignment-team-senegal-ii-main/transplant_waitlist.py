# Organ Transplant Waiting List
# Filename: transplant_waitlist.py
# Create a `TransplantWaitingList` class with:
# - `organ` (e.g., kidney, liver)
# - `patients` (list of names)
# Implement methods:
# - `add_patient(name)` → Adds a patient to the waiting list.
# - `remove_patient(name)` → Removes a patient when they receive a transplant.


class TransplantWaitingList:
    def __init__(self, organ):
        self.organ = organ  # Type of organ (e.g., kidney, liver)
        self.patients = []  # List to store patient names

    def add_patient(self, name):
        if name not in self.patients:
            self.patients.append(name)
            print(f"Patient {name} added to the {self.organ} transplant waiting list.")
        else:
            print(f"Patient {name} is already on the {self.organ} transplant waiting list.")

    def remove_patient(self, name):
        if name in self.patients:
            self.patients.remove(name)
            print(f"Patient {name} has been removed from the {self.organ} transplant waiting list.")
        else:
            print(f"Patient {name} is not on the {self.organ} transplant waiting list.")