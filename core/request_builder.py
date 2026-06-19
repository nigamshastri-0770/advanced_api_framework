class RequestBuilder:

    @staticmethod
    def build(
        token=None,
        body=None,
        params=None
    ):
        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return {
            "headers": headers,
            "json": body,
            "params": params
        }