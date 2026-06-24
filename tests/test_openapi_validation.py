from validators.openapi_validator import (
    OpenAPIValidator
)

from schemas.login_schema import (
    LOGIN_SCHEMA
)


def test_openapi_contract(
    apis
):

    response = (
        apis[
            "auth"
        ].login(
            "eve.holt@reqres.in",
            "cityslicka"
        )
    )

    assert (
        response.status_code
        == 200
    ), response.text

    body = (
        response.json()
    )

    assert (
        OpenAPIValidator.validate(
            body,
            LOGIN_SCHEMA
        )
        is True
    )