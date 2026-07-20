import requests

class CommentsApi:
    BASE_URL = "https://jsonplaceholder.typicode.com/comments"
    def get_comments(self):
        return requests.get(self.BASE_URL)

    def get_comment_by_id(self, comment_id):
        return requests.get(f'{self.BASE_URL}/{comment_id}')

