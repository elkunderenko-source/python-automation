import requests


class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all(self):
        return requests.get(self.base_url)

    def get_by_id(self, item_id):
        return requests.get(f"{self.base_url}/{item_id}")