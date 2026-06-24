import requests

from core.retry_handler import safe_request


class PaymentAPI:

    def __init__(
        self,
        base_url,
        api_key
    ):

        self.base_url = base_url

        self.headers = {
            "x-api-key": api_key
        }

    def get_user(
        self,
        user_id
    ):

        url = (
            f"{self.base_url}"
            f"/api/users/{user_id}"
        )

        return safe_request(
            "GET",
            url,
            headers=self.headers,
            timeout=20
        )

    def process(
        self,
        payload
    ):

        url = (
            f"{self.base_url}"
            "/api/payment"
        )

        return safe_request(
            "POST",
            url,
            headers=self.headers,
            json=payload,
            timeout=30
        )