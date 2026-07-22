from api.base.base_api import BaseApi


class CommentsApi(BaseApi):
    def __init__(self):
        super().__init__("https://jsonplaceholder.typicode.com/comments")
