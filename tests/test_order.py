# File: tests/test_order.py

from data.order_factory import (
OrderFactory
)

def test_create_order(
    apis
):
    payload = (
        OrderFactory
        .booking()
    )

    response = (
        apis["order"]
        .create_order(
            payload
        )
    )

    assert (
        response.status_code
        in [
            200,
            201
        ]
    )

    body = (
        response.json()
    )

    assert (
        isinstance(
            body,
            dict
        )
    )
