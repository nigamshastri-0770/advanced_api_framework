import requests


class UserAPI:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_users(self):
        return requests.get("https://jsonplaceholder.typicode.com/users")