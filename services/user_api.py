import requests

from core.service_registry import ServiceRegistry
from core.request_builder import RequestBuilder

class UserAPI:
    def profile(
        self,
        token
    ):
        url = (
            ServiceRegistry.get_url(
                "users"
            )
            + "/me"
        )

        req = RequestBuilder.build(
            token=token
        )

        return requests.get(
            url,
            **req
        )