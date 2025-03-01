def create_modalities_list():
    """
    Exercise 6: Basic List Operations
    Create a list with ["X-ray", "CT", "MRI", "Ultrasound"] and add "PET" to it.
    
    Returns:
        list: List of imaging modalities including PET
    """
    imaging_modalities = ["X-ray", "CT", "MRI", "Ultrasound"]
    imaging_modalities.append("PET")
    return imaging_modalities

    

def get_first_two_times():
    """
    Exercise 7: Indexing and Slicing Lists
    From scan_times = [12.5, 8.0, 15.2, 10.3], get the first two values.
    
    Returns:
        list: First two scan times
    """
    scan_times = [12.5, 8.0, 15.2, 10.3]
    return scan_times[:2]
   

def update_scan_quality():
    """
    Exercise 8: Modifying Lists
    In scan_quality = ["high", "medium", "low", "medium"], replace "low" with "high".
    
    Returns:
        list: Updated scan quality list
    """
    scan_quality = ["high", "medium", "low", "medium"]
    scan_quality[2] = "high"
    return scan_quality
    
    

def get_patient_info():
    """
    Exercise 9: Create a dictionary with patient info
    Keys: "ID" (101), "Name" ("Alice"), "Age" (45), "Modality" ("MRI")
    
    Returns:
        dict: Patient information dictionary
    """
    return {"ID": 101, "Name": "Alice", "Age": 45, "Modality": "MRI"}
    


def update_scan_parameters():
    """
    Exercise 10: Updating Dictionary Entries
    Update slice_thickness to 1.5 and contrast_used to True in the scan_parameters dictionary.
    
    Returns:
        dict: Updated scan parameters dictionary
    """
    scan_parameters = {
        "modality": "CT",
        "slice_thickness": 3.0,
        "contrast_used": False
    }
    scan_parameters["slice_thickness"] = 1.5
    scan_parameters["contrast_used"] = True
    return scan_parameters
    


def create_image_metadata():
    """
    Exercise 11: Create a dictionary with image metadata
    Keys: "resolution" ("512x512"), "scan_type" ("MRI"), "bit_depth" (16)
    
    Returns:
        dict: Image metadata dictionary
    """
    return {"resolution": "512x512", "scan_type": "MRI", "bit_depth": 16}
   


def create_patients_data():
    """
    Exercise 12: Create a nested dictionary for two patients
    Patient 101: {"Name": "Alice", "Age": 45, "Scan_Type": "MRI"}
    Patient 102: {"Name": "Bob", "Age": 50, "Scan_Type": "CT"}
    
    Returns:
        dict: Nested dictionary with patient data
    """
    return {
        101: {"Name": "Alice", "Age": 45, "Scan_Type": "MRI"},
        102: {"Name": "Bob", "Age": 50, "Scan_Type": "CT"}
    }

   