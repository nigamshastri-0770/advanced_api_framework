from core.api_client import APIClient


class NotificationAPI:

    def __init__(self):

        self.client = APIClient()

    def notify(self):

        return self.client.get("https://httpbin.org/headers")