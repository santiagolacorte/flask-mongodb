# Utilitary imports
import pytest

# Local imports
from src.services.employee import Employee


@pytest.fixture
def employee():
    """New 'Employee' instance for each test, thus
    isolating the tests from each other."""

    return Employee("1", "Smith", "Jack")

class TestEmployee:
    def test_employee_instance(self, employee):
        # ARRANGE & ACT: Already done through pytest.fixture

        # ASSERT
        assert employee.employee_id == "1"
        assert employee.last_name == "Smith"
        assert employee.name == "Jack"

    def test_employee_str(self, employee):
        # ARRANGE: Already done through pytest.fixture

        # ACT
        result = str(employee)

        # ASSERT
        assert result == "Jack Smith"

    def test_employee_to_dict(self, employee):
        # ARRANGE: Already done through pytest.fixture

        # ACT
        result = employee.to_dict()

        # ASSERT
        assert result == {
            "employee_id": "1",
            "last_name": "Smith",
            "name": "Jack"
        }

    def test_null_employee_to_dict(self, employee):
        # ARRANGE: Already done through pytest.fixture

        # ACT
        employee.name = None

        # ASSERT
        with pytest.raises(ValueError) as exc_info:
            str(employee)
        assert str(exc_info.value) == "Name or Last Name cannot be None"
