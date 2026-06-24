import pytest

@pytest.mark.serial
def test_microservices_flow(apis):

    auth = apis["auth"]

    login = auth.login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    assert login.status_code in [200, 201]