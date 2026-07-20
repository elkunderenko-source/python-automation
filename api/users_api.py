import requests

class UsersApi:
    BASE_URL = "http://jsonplaceholder.typicode.com/users"

    def get_users(self):
        return requests.get(self.BASE_URL)


    def get_user_by_id(self, user_id):
        return requests.get(f"{self.BASE_URL}/{user_id}")

class AlbumsApi:
    BASE_URL = "https://jsonplaceholder.typicode.com/albums"

    def get_albums(self):
        return requests.get(self.BASE_URL)

    def get_album_by_id(self, id):
        return requests.get(f"{self.BASE_URL}/{id}")

    def get_album_by_userid(self, user_id):
        return requests.get(f"{self.BASE_URL}?userId={user_id}")

