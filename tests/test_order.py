from services.order_api import (
    OrderAPI
)

def test_create_order():
    api = (
        OrderAPI()
    )

    response = (
        api.create(
            "demo",
            {
                "product": "Laptop"
            }
        )
    )

    assert (
        response.status_code
        == 200
    )

