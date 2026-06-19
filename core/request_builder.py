class RequestBuilder:

    @staticmethod
    def build(
        token=None,
        payload=None,
        params=None,
        headers=None
    ):

        req_headers = {
            "Content-Type": "application/json"
        }

        if headers:
            req_headers.update(headers)

        if token:
            req_headers[
                "Authorization"
            ] = f"Bearer {token}"

        return {
            "headers": req_headers,
            "json": payload,
            "params": params
        }