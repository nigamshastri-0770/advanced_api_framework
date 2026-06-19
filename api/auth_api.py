import requests

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

        return requests.post(url, json=payload, headers=self.headers)