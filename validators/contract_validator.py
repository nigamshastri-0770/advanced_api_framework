# File: validators/contract_validator.py

from jsonschema import validate


class ContractValidator:

    @staticmethod
    def validate_response(
        response,
        schema
    ):

        body = (
            response.json()
        )

        validate(
            instance=body,
            schema=schema
        )

        return True