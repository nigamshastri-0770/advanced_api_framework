from services.gateway_api import (
    GatewayAPI
)

class OrderAPI:
    def create(
        self,
        token,
        payload
    ):
        return GatewayAPI.fake_response(
            {
                "order_id": 101,
                "status": "created"
            }
        )
