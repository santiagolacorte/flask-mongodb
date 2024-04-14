class Employee:
    """Represents an employee with an ID, last name, and first name.
    
    This class is used to model employee data for manipulation and storage in the database. 
    It includes a method to serialize the employee object to a dictionary format.
    
    Attributes:
    - employee_id (str): Unique identifier for the employee.
    - last_name (str): The employee's last name.
    - name (str): The employee's first name."""
    
    def __init__(self, employee_id, last_name, name) -> None:
        self.employee_id = employee_id
        self.last_name = last_name
        self.name = name


    def __str__(self) -> str:
        if self.name and self.last_name:
            return f"{self.name} {self.last_name}"
        else:
            raise ValueError("Name or Last Name cannot be None")


    def to_dict(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "last_name": self.last_name,
            "name": self.name
        }
