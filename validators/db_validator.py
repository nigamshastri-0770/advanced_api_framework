# File: validators/db_validator.py

class DBValidator:
    @staticmethod
    def validate_equal(
        api_value,
        db_value
    ):
        assert (
            api_value
            ==
            db_value
        ), (
            f"Mismatch → "
            f"API={api_value} "
            f"DB={db_value}"
        )

