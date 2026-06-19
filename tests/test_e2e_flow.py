from services.auth_api import (
AuthAPI
)

from services.order_api import (
OrderAPI
)

from services.payment_api import (
PaymentAPI
)

def test_microservices_flow():
    token = (
        AuthAPI()
        .login(
            "demo@test.com",
            "123"
        )
        .json()["token"]
    )

    order = (
        OrderAPI()
        .create(
            token,
            {}
        )
    )

    assert (
        order.status_code
        == 200
    )

    payment = (
        PaymentAPI()
        .process(
            token,
            {}
        )
    )

    assert (
        payment.status_code
        == 200
    )
