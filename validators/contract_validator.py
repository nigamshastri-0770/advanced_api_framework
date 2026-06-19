from openapi_core import validate_response # type: ignore

class ContractValidator:

    @staticmethod
    def validate(
        response
    ):
        validate_response(
            response
        )

        return True