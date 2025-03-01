def basic_variable():
    """
    Exercise 1: Basic Variable Assignment
    Define a variable modality and assign it the value "MRI". Then, return its type.
    
    Returns:
        type: The type of the variable modality
    """
    modality = "MRI"
    return type(modality)


def calculate_mri_difference():
    """
    Exercise 2: Numeric Operations
    Calculate the difference in field strength between research MRI (7.0T) and clinical MRI (1.5T).
    
    Returns:
        float: The difference in Tesla between research MRI and clinical MRI
    """
    clinical_mri = 1.5  # Tesla
    research_mri = 7.0  # Tesla
    return research_mri - clinical_mri
    


def modify_scan_type():
    """
    Exercise 3: String Manipulation
    Given scan_type = "functional MRI", convert it to uppercase and replace "FUNCTIONAL" with "FMRI".
    
    Returns:
        str: The modified scan type string
    """
    scan_type = "functional MRI"
    modified_scan_type = scan_type.upper().replace("FUNCTIONAL", "FMRI")
    return modified_scan_type
    

def check_abnormality():
    """
    Exercise 4: Boolean Variables
    Check abnormality_detected (True) and return appropriate message:
    - If True: "Abnormality detected in the CT scan. Further investigation required."
    - If False: "No abnormalities detected in the CT scan."
    
    Returns:
        str: Message indicating whether abnormality was detected
    """
    abnormality_detected = True
    if abnormality_detected:
        return "Abnormality detected in the CT scan. Further investigation required."
    else:
        return "No abnormalities detected in the CT scan."


def convert_suv():
    """
    Exercise 5: Type Conversion
    Convert suv = "3.8" to float and increase by 10%.
    
    Returns:
        float: The adjusted SUV value
    """
    suv = "3.8"
    suv_float = float(suv)
    return suv_float * 1.1

