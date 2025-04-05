# Medical Imaging Analysis System
# Filename: mri_scan.py
# Create an `MRI_Scan` class with:
# - `patient_name`
# - `scan_date`
# - `findings` (default `None`)
# Implement methods:
# - `add_findings(report)` → Updates the scan findings.
# - `get_scan_details()` → Returns patient name, date, and findings.


class MRI_Scan:
    def __init__(self, patient_name, scan_date):
        self.patient_name = patient_name
        self.scan_date = scan_date
        self.findings = None  # Default to no findings

    def add_findings(self, report):
        self.findings = report
        print(f"Findings updated for {self.patient_name}'s MRI scan on {self.scan_date}.")

    def get_scan_details(self):
        return {
            "Patient Name": self.patient_name,
            "Scan Date": self.scan_date,
            "Findings": self.findings
        }