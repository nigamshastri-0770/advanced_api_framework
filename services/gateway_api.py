class FakeResponse:
    def __init__(self, data):
        self.data = data
        self.status_code = 200

    def json(self):
        return self.data


class GatewayAPI:
    @staticmethod
    def fake_response(body):
        return FakeResponse(body)
