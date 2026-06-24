import responses # pyright: ignore[reportMissingImports]


@responses.activate
def test_auth_login(apis):

    responses.add(
        method=responses.POST,
        url="https://reqres.in/api/login",
        json={"token": "fake-token"},
        status=200
    )

    response = apis["auth"].login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    assert response.status_code == 200
    assert response.json()["token"] == "fake-token"