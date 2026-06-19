# File: tests/test_allure_reporting.py

from utils.allure_helper import AllureHelper


def test_allure_reporting(apis):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }

    AllureHelper.attach_request("/api/login", payload)

    response = (
        apis["auth"].login(payload["email"], payload["password"])
    )

    AllureHelper.attach_response(response)

    assert response.status_code == 200

    body = response.json()

    assert "token" in body

