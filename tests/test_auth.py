def test_auth_login(apis):
    response = apis["auth"].login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    print("URL →", response.url)
    print("Status →", response.status_code)

    assert response.status_code == 200
    assert "token" in response.json()