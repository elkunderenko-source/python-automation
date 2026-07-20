from api.posts_api import PostsApi
import pytest

USER_ID = 9
payload = {
    "title": "Pytest training",
    "body": "Learning API testing",
    "userId": 9
}


@pytest.fixture
def api():
    # print("Creating API")
    return PostsApi()


@pytest.fixture
def create_post_response(api):
    return api.create_post(payload)


def test_status_code(api):
    response = api.get_posts_by_user(USER_ID)
    assert response.status_code == 200


def test_posts_by_user(api):
    response = api.get_posts_by_user(USER_ID)
    assert len(response.json()) == 10
    assert isinstance(response.json(), list)


def test_new_post(create_post_response):
    response_data = create_post_response.json()
    assert create_post_response.status_code == 201
    assert 'id' in response_data
    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]
    assert response_data["userId"] == payload["userId"]
    assert isinstance(response_data, dict)





