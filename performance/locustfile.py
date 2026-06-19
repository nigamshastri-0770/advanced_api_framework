# File: performance/locustfile.py

from locust import HttpUser # pyright: ignore[reportMissingImports]
from locust import task # type: ignore
from locust import between # pyright: ignore[reportMissingImports]

class APIUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://reqres.in"
    headers = {
        "x-api-key": "free_user_3EqwNfJjHbaSI4VWRBchJllgjn9"
    }

    @task(2)
    def login(self):
        self.client.post(
            "/api/login",
            json={
                "email": "eve.holt@reqres.in",
                "password": "cityslicka",
            },
            headers=self.headers,
        )

    @task(1)
    def users(self):
        self.client.get(
            "/api/users?page=2",
            headers=self.headers,
        )

