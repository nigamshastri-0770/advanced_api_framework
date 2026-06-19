from services.payment_api import (
    PaymentAPI
)

def test_payment_flow():
    api = (
        PaymentAPI()
    )

    response = (
        api.process(
            "demo_token",
            {
                "amount": 500
            }
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
        body["success"]
        is True
)
