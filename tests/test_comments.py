
from api.comments_api import CommentsApi
import pytest

@pytest.fixture
def comments_api():
    return CommentsApi()

def test_get_comments_by_id(comments_api):
    response = comments_api.get_comments()
    assert response.status_code == 200
    comments = response.json()
    for comment in comments:
        if comment['email'] == "Eliseo@gardner.biz":
            comment_from_list = comment
            break
    assert comment_from_list is not None
    comment_response = comments_api.get_comment_by_id(comment_from_list["id"])
    comment = comment_response.json()
    assert comment_from_list['id'] == comment.get('id')
    assert comment_from_list['name'] == comment.get('name')
    assert comment_from_list['email'] == comment.get('email')
    assert comment_from_list['body'] == comment.get('body')