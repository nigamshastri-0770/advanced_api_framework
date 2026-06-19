class StatusValidator:

    @staticmethod
    def validate(
        response,
        expected
    ):
        actual = response.status_code

        assert (
            actual
            == expected
        ), (
            f"Expected {expected} "
            f"but got {actual}"
        )
