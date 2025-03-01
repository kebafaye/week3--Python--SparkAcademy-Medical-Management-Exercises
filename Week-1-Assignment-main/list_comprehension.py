def generate_scan_ids():
    """
    Exercise 13: Generate a list of scan IDs from 1001 to 1010 using list comprehension.
    
    Returns:
        list: List of scan IDs from 1001 to 1010
    """
    scan_ids = [i for i in range(1001, 1011)]
    return scan_ids



def filter_scan_times():
    """
    Exercise 14: Given scan_times = [5.2, 12.8, 9.3, 15.1, 7.4],
    use list comprehension to create a new list with times greater than 10 minutes.
    
    Returns:
        list: List of scan times greater than 10 minutes
    """
    scan_times = [5.2, 12.8, 9.3, 15.1, 7.4]
    long_scans = [time for time in scan_times if time > 10]
    return long_scans
    


def extract_patient_names():
    """
    Exercise 15: Given a list of patient dictionaries, extract all patient names using list comprehension.
    
    Returns:
        list: List of patient names
    """
    patients = [
        {"Name": "Alice", "Age": 45},
        {"Name": "Bob", "Age": 60},
        {"Name": "Charlie", "Age": 35}
    ]
    patient_names = [patient["Name"] for patient in patients]
    return patient_names


def get_image_widths():
    """
    Exercise 16: Given resolutions = ["256x256", "512x512", "1024x1024"],
    extract only the width values as integers using list comprehension.
    
    Returns:
        list: List of width values as integers
    """
    resolutions = ["256x256", "512x512", "1024x1024"]
    widths = [int(res.split('x')[0]) for res in resolutions]
    return widths
    
    


def classify_suv_values():
    """
    Exercise 17: Given SUV values, classify them as "high" if > 3.5, otherwise "low".
    
    Returns:
        list: List of classifications ("high" or "low")
    """
    suv_values = [2.3, 4.1, 1.8, 5.6, 3.9]
    classifications = ["high" if value > 3.5 else "low" for value in suv_values]
    return classifications


def generate_report_titles():
    """
    Exercise 18: Create report titles for each modality (e.g., "MRI Report", "CT Report").
    
    Returns:
        list: List of report titles
    """
    modalities = ["MRI", "CT", "X-ray"]
    reports = [f"{modality} Report" for modality in modalities]
    return reports
    
    


def filter_scan_durations():
    """
    Exercise 19: Filter out scan times greater than 30 minutes.
    
    Returns:
        list: List of scan durations <= 30 minutes
    """
    scan_durations = [20, 25, 30, 12, 40, 15]
    filtered_times = [duration for duration in scan_durations if duration <= 30]
    return filtered_times
    


def get_even_indexed_slices():
    """
    Exercise 20: Extract values at even indices from slice_thicknesses.
    
    Returns:
        list: List of values at even indices
    """
    slice_thicknesses = [1.5, 3.0, 2.5, 4.0, 5.0, 6.5]
    even_indexed = [slice_thicknesses[i] for i in range(0, len(slice_thicknesses), 2)]
    return even_indexed
    
   