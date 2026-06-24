from unittest.mock import patch
from services.payment_api import PaymentAPI


@patch("services.payment_api.safe_request")
def test_payment_flow(mock_request):

    class MockResponse:
        status_code = 200

        def json(self):
            return {
                "success": True
            }

    mock_request.return_value = MockResponse()

    api = PaymentAPI(
        base_url="https://fake-api.com",
        api_key="demo_key"
    )

    response = api.process(
        {
            "amount": 500
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True