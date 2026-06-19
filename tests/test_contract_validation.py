# File: tests/test_contract_validation.py

from schemas.login_schema import (
    LOGIN_SCHEMA
)

from validators.contract_validator import (
    ContractValidator
)


def test_login_contract(
    apis
):

    response = (
        apis["auth"]
        .login(
            "eve.holt@reqres.in",
            "cityslicka"
        )
    )

    assert (
        response.status_code
        == 200
    )

    ContractValidator.validate_response(
        response,
        LOGIN_SCHEMA
    )