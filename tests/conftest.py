import pytest
from api.posts_api import PostsApi
from api.users_api import UsersApi
from api.users_api import AlbumsApi
from api.comments_api import CommentsApi

@pytest.fixture
def api():
    # print("Creating API")
    return PostsApi('https://jsonplaceholder.typicode.com/posts')

@pytest.fixture
def api_users():
    return UsersApi()


@pytest.fixture
def album_api():
    return AlbumsApi()

@pytest.fixture
def comments_api():
    return CommentsApi()