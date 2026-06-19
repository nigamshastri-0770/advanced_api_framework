def test_create_order(apis):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = apis["order"].create_order(payload)

    print("Status →", response.status_code)
    print("Response →", response.json())

    assert response.status_code == 201
    assert "id" in response.json()