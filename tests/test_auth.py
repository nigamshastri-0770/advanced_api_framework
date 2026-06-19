from services.auth_api import AuthAPI
from validators.status_validator import StatusValidator

def test_auth_login():
    api = AuthAPI()

    response = api.login(
        "demo@test.com",
        "Password123"
    )

    StatusValidator.validate(
        response,
        200
    )
