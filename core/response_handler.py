class ResponseHandler:

    @staticmethod
    def json(response):
        return response.json()

    @staticmethod
    def status(response):
        return response.status_code