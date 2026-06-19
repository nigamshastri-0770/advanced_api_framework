class DBValidator:

    @staticmethod
    def compare(
        api_data,
        db_data
    ):
        assert (
            api_data
            == db_data
        ), (
            "DB Validation Failed"
        )

        return True
