# Local imports
from src.services.employee import Employee

class TestEmployee:
    def test_employee_instance(self):
        # ARRANGE
        employee = Employee("1", "Smith", "Jack")

        # ACT
        result = employee

        # ASSERT
        assert result.employee_id == "1"
        assert result.last_name == "Smith"
        assert result.name == "Jack"

    def test_employee_str(self):
        # ARRANGE
        employee = Employee("1", "Smith", "Jack")

        # ACT
        result = str(employee)

        # ASSERT
        assert result == "Jack Smith"

    def test_employee_to_dict(self):
        # ARRANGE
        employee = Employee("1", "Smith", "Jack")

        # ACT
        result = employee.to_dict()

        # ASSERT
        assert result == {
            "employee_id": "1",
            "last_name": "Smith",
            "name": "Jack"
        }
