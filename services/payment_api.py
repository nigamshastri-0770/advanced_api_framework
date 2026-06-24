from core.retry_handler import safe_request


class PaymentAPI:

    def __init__(
        self,
        base_url,
        api_key=None
    ):
        self.base_url = base_url

    def process(
        self,
        payload
    ):

        url = (
            f"{self.base_url}/api/users"
        )

        return safe_request(
            "POST",
            url,
            json=payload
        )