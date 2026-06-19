class ResponseValidator:
    @staticmethod
    def contains(response, key):
        body = response.json()
        assert key in body

    @staticmethod
    def value(response, key, expected):
        body = response.json()
        assert body[key] == expected