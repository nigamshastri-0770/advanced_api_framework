from openapi_core import validate_response


class ContractValidator:

    @staticmethod
    def validate(resp):
        validate_response(resp)