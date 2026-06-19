import json


class ResponseHandler:

    @staticmethod
    def json(response):

        try:
            return response.json()

        except Exception:
            return {}

    @staticmethod
    def text(response):

        return response.text

    @staticmethod
    def status(response):

        return response.status_code

    @staticmethod
    def pretty(response):

        try:
            return json.dumps(
                response.json(),
                indent=4
            )

        except Exception:
            return response.text

    @staticmethod
    def success(response):

        return (
            200
            <= response.status_code
            < 300
        )