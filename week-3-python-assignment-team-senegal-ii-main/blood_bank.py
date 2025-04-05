# Blood Bank Management System
# Filename: blood_bank.py
# Create a `BloodBank` class with:
# - `blood_type`
# - `units_available`
# Implement methods:
# - `donate_blood(units)` → Increases the units available.
# - `request_blood(units)` → Decreases units if enough stock exists.


class BloodBank:
    def __init__(self, blood_type, units_available):
        self.blood_type = blood_type
        self.units_available = units_available

    def donate_blood(self, units):
        if units > 0:
            self.units_available += units
            print(f"Donated {units} units of {self.blood_type} blood. Total units available: {self.units_available}")
        else:
            print("Invalid number of units to donate.")

    def request_blood(self, units):
        if units > 0:
            if self.units_available >= units:
                self.units_available -= units
                print(f"Requested {units} units of {self.blood_type} blood. Remaining units: {self.units_available}")
            else:
                print(f"Not enough {self.blood_type} blood available. Only {self.units_available} units left.")
        else:
            print("Invalid number of units to request.")