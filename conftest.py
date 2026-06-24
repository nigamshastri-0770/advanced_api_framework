import pytest

from core.context import Context

from services.auth_api import AuthAPI
from services.user_api import UserAPI
from services.order_api import OrderAPI
from services.payment_api import PaymentAPI
from services.notification_api import NotificationAPI


@pytest.fixture
def ctx():
    return Context()


@pytest.fixture
def apis():
    return {
        "auth": AuthAPI(),
        "user": UserAPI(),
        "order": OrderAPI(),
        "payment": PaymentAPI(),
        "notification": NotificationAPI()
    }