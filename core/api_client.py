import requests
from tenacity import retry, stop_after_attempt, wait_fixed


class APIClient:

    def __init__(self):
        self.session = requests.Session()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def get(self, url, headers=None, params=None):

        response = self.session.get(
            url,
            headers=headers,
            params=params
        )

        self._log(response)

        return response

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def post(self, url, payload=None, headers=None):

        response = self.session.post(
            url,
            json=payload,
            headers=headers
        )

        self._log(response)

        return response

    def _log(self, response):

        print(f"URL → {response.url}")
        print(f"Status → {response.status_code}")
        print(f"Time → {response.elapsed.total_seconds()}s")