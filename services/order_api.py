from core.retry_handler import safe_request

class OrderAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def create_order(self, payload):
        url = f"{self.base_url}/api/users"

        return safe_request(
            "POST",
            url,
            json=payload,
            headers=self.headers
        )