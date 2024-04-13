# Utilitary imports
from flask import Blueprint, jsonify, render_template, Response

# Local imports
from ..services.services import get_employee, get_employees, post_employee


employees = Blueprint("employees", __name__)


@employees.route("/<string:employee_id>", methods=["GET"])
def get_employee_route(employee_id: str) -> str:
    """Fetches an employee's data by ID and renders a HTML page.

    Args:
    - employee_id (str): The ID of the employee to retrieve.

    Returns:
    - str: A HTML page with the employee's data.
    
    Raises:
    - Exception: if no employee is found with the provided ID.
    - OperationFailure: If a database operation fails.
    - Exception For any other errors encountered.
    - ValueError: If 'employee_id' does not match the expected format."""

    try:
        employee = get_employee(employee_id)
        return render_template("pages/employee.html", employee=employee)
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        message = str(e)

        if "not found" in message.lower():
            return jsonify({"error": message}), 404
        
        else:
            return jsonify({"error": message}), 500


@employees.route("/", methods=["GET"])
def get_employees_route() -> str:
    """Fetches and displays data for all employees.

    Returns:
    - str: A HTML page listing all employees.

    Raises:
    - OperationFailure: If a database operation fails.
    - Exception: For any other errors encountered."""

    try:
        employees = get_employees()
        return render_template("pages/employees.html", employees=employees)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500 



@employees.route("/", methods=["POST"])
def post_employee_route() -> Response:
    """Creates a new employee with data from a POST request.
    
    Returns: 
    - Response: A JSON object with the new employee's data and a status code.
    
    Raises:
    - ValueError: If required data is missing or 'employee_id' is invalid.
    - OperationFailure: If a database operation fails.
    - Exception: For any other errors encountered."""

    try:
        response, status = post_employee()
        return jsonify(response), status
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
