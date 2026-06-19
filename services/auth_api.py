import requests

from services.gateway_api import (
GatewayAPI
)

class AuthAPI:
    def login(
        self,
        email,
        password
    ):
        return GatewayAPI.fake_response(
            {
                "token":
                "demo_token",

                "user": {
                    "email":
                    email
                }
            }
        )

