import requests

from core.service_registry import ServiceRegistry

class NotificationAPI:
    def send(
        self,
        token,
        order_id
    ):
        url = (
            ServiceRegistry.get_url(
                "notifications"
            )
            + "/send"
        )

        return requests.post(
            url,
            headers={
                "Authorization":
                f"Bearer {token}"
            },
            json={
                "order_id":
                order_id
            }
        )