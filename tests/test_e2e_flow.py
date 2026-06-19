def test_microservices_flow(apis):
    login = apis["auth"].login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    assert login.status_code == 200

    users = apis["payment"].get_user(2)

    assert users.status_code == 200