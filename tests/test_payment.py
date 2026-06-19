def test_payment_flow(apis):
    response = apis["payment"].get_user(2)

    print("Status →", response.status_code)

    assert response.status_code == 200