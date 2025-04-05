# Vital Signs Monitoring System
# Filename: vital_signs.py
# Create a `VitalSigns` class with:
# - `patient_name`
# - `heart_rate`
# - `blood_pressure`
# Implement methods:
# - `update_vitals(hr, bp)` → Updates heart rate and blood pressure.
# - `is_critical()` → Returns `True` if heart rate < 50 or > 120, or blood pressure is too high/low.
# Vital Signs Monitoring System
# Filename: vital_signs.py



class VitalSigns:
    def __init__(self, patient_name, heart_rate, blood_pressure):
        self.patient_name = patient_name
        self.heart_rate = heart_rate
        # Convertir la pression artérielle en tuple si elle est fournie sous forme de chaîne
        if isinstance(blood_pressure, str):
            systolic, diastolic = blood_pressure.split('/')
            self.blood_pressure = (int(systolic), int(diastolic))
        else:
            self.blood_pressure = blood_pressure  # Supposons que c'est déjà un tuple

    def update_vitals(self, hr, bp):
        self.heart_rate = hr
        # Convertir la pression artérielle en tuple si elle est fournie sous forme de chaîne
        if isinstance(bp, str):
            systolic, diastolic = bp.split('/')
            self.blood_pressure = (int(systolic), int(diastolic))
        else:
            self.blood_pressure = bp  # Supposons que c'est déjà un tuple
        print(f"Vitals updated for {self.patient_name}: HR = {hr}, BP = {self.blood_pressure}.")

    def is_critical(self):
        # Définir les conditions critiques
        critical_hr = self.heart_rate < 50 or self.heart_rate > 120
        critical_bp = self.blood_pressure[0] < 90 or self.blood_pressure[1] > 140  # Seuils hypothétiques

        if critical_hr or critical_bp:
            return True
        else:
            return False