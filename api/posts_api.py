import requests
from api.base.base_api import BaseApi


class PostsApi(BaseApi):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_posts_by_user(self, user_id):
        return requests.get(f'{self.base_url}?userId={user_id}')

    def create_post(self, payload):
        return requests.post(url=self.base_url, json=payload)