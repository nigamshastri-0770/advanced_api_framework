# File: tests/test_auth.py

def test_auth_login(
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

    body = (
        response.json()
    )

    assert (
        "token"
        in body
    )
