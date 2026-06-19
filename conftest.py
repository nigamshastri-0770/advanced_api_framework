import pytest
from api.auth_api import AuthAPI
from api.order_api import OrderAPI
from api.payment_api import PaymentAPI

API_KEY = "free_user_3EqwNfJjHbaSI4VWRBchJllgjn9"


@pytest.fixture
def api_base_url():
    return "https://reqres.in"


@pytest.fixture
def api_key():
    return API_KEY


@pytest.fixture
def apis(api_base_url, api_key):
    return {
        "auth": AuthAPI(api_base_url, api_key),
        "order": OrderAPI(api_base_url, api_key),
        "payment": PaymentAPI(api_base_url, api_key),
    }