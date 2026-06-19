import requests

class PaymentAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {"x-api-key": api_key}

    def get_user(self, user_id):
        url = f"{self.base_url}/api/users/{user_id}"
        return requests.get(url, headers=self.headers)