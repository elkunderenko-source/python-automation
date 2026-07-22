import requests
from api.base.base_api import BaseApi

class UsersApi(BaseApi):
    def __init__(self):
        super().__init__("http://jsonplaceholder.typicode.com/users")

class AlbumsApi(BaseApi):
    def __init__(self):
        super().__init__("http://jsonplaceholder.typicode.com/albums")

    def get_album_by_userid(self, user_id):
        return requests.get(f"{self.base_url}?userId={user_id}")

