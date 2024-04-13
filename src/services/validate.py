# Utilitary imports
import re


def id_verified(employee_id: str) -> bool:
    """Validate the 'employee_id' parameter with the expected regex pattern.
    
    Args:
    - employee_id: Argument to validate.
    
    Returns: True if 'employee_id' is valid, False otherwise."""

    pattern = r"^\d{8}-\d$"

    if re.match(pattern, employee_id):
        return True
