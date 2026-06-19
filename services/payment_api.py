from services.gateway_api import (
    GatewayAPI
)

class PaymentAPI:
    def process(
        self,
        token,
        payload
    ):
        return GatewayAPI.fake_response(
            {
                "payment_id": 501,
                "success": True
            }
        )
