# Local imports
from src.services.validate import id_verified


class TestValidate:
    def test_successful_validate(self):
        # ARRANGE
        employee_id = "12345678-9"

        # ACT
        result = id_verified(employee_id)

        # ASSERT
        assert result is True

    def test_unsuccessful_validate(self):
        # ARRANGE
        employee_id = "12345678"

        # ACT
        result = id_verified(employee_id)

        # ASSERT
        assert result is None
