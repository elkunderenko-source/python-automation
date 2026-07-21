import requests


class BaseApi:

    def get_all(self):
        return requests.get(self.BASE_URL)

    def get_by_id(self, item_id):
        return requests.get(f"{self.BASE_URL}/{item_id}")