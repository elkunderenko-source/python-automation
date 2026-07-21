import requests
from api.base.base_api import BaseApi

class UsersApi(BaseApi):
    BASE_URL = "http://jsonplaceholder.typicode.com/users"

class AlbumsApi(BaseApi):
    BASE_URL = "https://jsonplaceholder.typicode.com/albums"

    def get_album_by_userid(self, user_id):
        return requests.get(f"{self.BASE_URL}?userId={user_id}")

