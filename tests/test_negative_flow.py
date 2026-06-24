import pytest

from services.auth_api import AuthAPI
from services.order_api import OrderAPI
from services.payment_api import PaymentAPI


BASE_URL = "https://httpbin.org"
VALID_KEY = "demo_key"
INVALID_KEY = "wrong_key"


# ==========================
# AUTH NEGATIVE
# ==========================

def test_login_invalid_credentials():

    api = AuthAPI(
        BASE_URL,
        INVALID_KEY
    )

    response = api.login(
        "wrong_user",
        "wrong_pass"
    )

    assert response.status_code in [
        401,
        403,
        404,
        503
    ]


def test_login_empty_credentials():

    api = AuthAPI(
        BASE_URL,
        VALID_KEY
    )

    response = api.login(
        "",
        ""
    )

    assert response.status_code in [
        400,
        401,
        404,
        503
    ]


# ==========================
# PAYMENT NEGATIVE
# ==========================

def test_payment_invalid_key():

    api = PaymentAPI(
        BASE_URL,
        INVALID_KEY
    )

    response = api.process(
        {
            "amount": 500
        }
    )

    assert response.status_code in [
        401,
        403,
        404,
        503
    ]


def test_payment_negative_amount():

    api = PaymentAPI(
        BASE_URL,
        VALID_KEY
    )

    response = api.process(
        {
            "amount": -100
        }
    )

    assert response.status_code in [
        400,
        404,
        422,
        503
    ]


def test_payment_empty_payload():

    api = PaymentAPI(
        BASE_URL,
        VALID_KEY
    )

    response = api.process(
        {}
    )

    assert response.status_code in [
        400,
        404,
        422,
        503
    ]


# ==========================
# NETWORK FAILURE
# ==========================

def test_invalid_host():

    api = PaymentAPI(
        "https://invalid-host-123.com",
        VALID_KEY
    )

    with pytest.raises(Exception):

        api.process(
            {
                "amount": 100
            }
        )