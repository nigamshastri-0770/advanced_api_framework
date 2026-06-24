from core.retry_handler import safe_request

class AuthAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def login(self, email, password):
        url = f"{self.base_url}/api/login"

        payload = {
            "email": email,
            "password": password
        }

        return safe_request(
            "POST",
            url,
            json=payload,
            headers=self.headers
        )