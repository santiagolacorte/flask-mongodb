# Utilitary imports
from flask import request
import logging
import pymongo

# Local imports
from ..config.mongodb import mongo
from .employee import Employee
from .validate import id_verified


def get_employee(employee_id: str) -> dict:
    """Retrieves an employee's data from the database by ID.

    Args:
    - employee_id (str): The ID of the employee to be retrieved.

    Returns: 
    - dict: A dictionary containing the employee's data, if found.

    Raises:
    - Exception: If no employee is found with the provided ID.
    - OperationFailure: If a database operation fails.
    - Exception: For any other errors encountered.
    - ValueError: If 'employee_id' is invalid."""

    if id_verified(employee_id):
        try:
            employee = mongo.db.employees.find_one({"employee_id": employee_id})

            if employee:
                employee["_id"] = str(employee["_id"])

                return employee
            
            else:
                raise Exception(f"Employee with ID '{employee_id}' not found.")
        
        except pymongo.errors.OperationFailure as e:
            raise Exception(f"Operation failure: {str(e)}")
        
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
    
    else:
        raise ValueError("Invalid employee ID format.")


def get_employees() -> list:
    """Retrieves data for all employees from the database.

    Returns: 
    - list: A list of dictionaries, each representing an employee.
    
    Raises:
    - OperationFailure: If a database operation fails.
    - Exception: For any other errors encountered."""

    try:
        employees = mongo.db.employees.find()
        employees_list = []

        for employee in employees:
            employee["_id"] = str(employee["_id"])
            employees_list.append(employee)
        
        return employees_list
    
    except pymongo.errors.OperationFailure as e:
        raise Exception(f"Operation failure: {str(e)}")
    
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")


def post_employee() -> tuple:
    """Creates a new employee in the database using data from a POST request.

    Returns:
    - tuple: A tuple of a dictionary with the operation's 
    outcome and a status code.

    Raises:
    - 400: If required data is missing or 'employee_id' is invalid.
    - 409: If an employee with the provided ID already exists.
    - 500: If a database operation fails or any other error encountered."""

    try:
        data = request.get_json()

        employee_id = data.get("employee_id", "").strip()
        last_name = data.get("last_name", "").strip()
        name = data.get("name", "").strip()

        if not employee_id or not last_name or not name:
            logging.error("Missing required employee information")
            return {"status": "failure", "message": "Missing required employee information"}, 400

        if id_verified(employee_id):
            existing_employee = mongo.db.employees.find_one({"employee_id": employee_id})

            if existing_employee:
                logging.error(f"Employee with ID '{employee_id}' already exists.")
                return {"status": "failure", "message": f"Employee with ID '{employee_id}' already exists."}, 409

            employee = Employee(
                employee_id=employee_id,
                last_name=last_name,
                name=name,
            )

            mongo.db.employees.insert_one(employee.to_dict())

            return {"status": "success", "message": "Employee inserted successfully to the DB."}, 201
        
        else:
            logging.error("Invalid employee ID format.")
            return {"status": "failure", "message": "Invalid employee ID format."}, 400
    
    except pymongo.errors.OperationFailure as e:
        logging.exception("Operation failure:", exc_info=e)
        return {"status": "failure", "message": "Database operation failed"}, 500
    
    except Exception as e:
        logging.exception("Unexpected error:", exc_info=e)
        return {"status": "failure", "message": "An unexpected error occurred"}, 500
