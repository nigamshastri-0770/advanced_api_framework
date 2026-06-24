import responses # pyright: ignore[reportMissingImports]


@responses.activate
def test_create_order(apis):

    responses.add(
        method=responses.POST,
        url="https://reqres.in/api/users",
        json={"id": "123"},
        status=201
    )

    response = apis["order"].create_order(
        {"name": "Nigam"}
    )

    assert response.status_code == 201