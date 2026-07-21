import requests
from api.base.base_api import BaseApi


class PostsApi(BaseApi):
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    def get_posts_by_user(self, user_id):
        return requests.get(f'{self.BASE_URL}?userId={user_id}')

    def create_post(self, payload):
        return requests.post(url=self.BASE_URL, json=payload)