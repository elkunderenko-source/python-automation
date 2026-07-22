import pytest
import json
def test_users_api(api_users):
    response = api_users.get_all()
    user_data = response.json()
    assert response.status_code == 200
    assert isinstance(user_data, list)
    assert len(user_data) == 10
    for user in user_data:
        assert 'id' in user
        assert 'name' in user
        assert 'username' in user
        assert 'email' in user
        assert 'address' in user
        assert 'phone' in user
        assert 'website' in user
        assert 'company' in user
        assert isinstance(user['id'], int)
        assert isinstance(user['name'], str)
        assert isinstance(user['username'], str)
        assert isinstance(user['email'], str)
        assert '@' in user['email']


def test_user_from_list_matches_single_user(api_users):
    user_from_list = None
    response = api_users.get_all()
    users = response.json()
    for user in users:
        if user['username'] == "Bret":
            user_from_list = user
            break

    user_data = api_users.get_by_id(user_from_list["id"]).json()
    assert user_data['username'] == user_from_list['username']
    assert user_data['address']['street'] == user_from_list['address']['street']
    assert user_data['address']['suite'] == user_from_list['address']['suite']
    assert user_data['address']['city'] == user_from_list['address']['city']
    assert user_data['address']['zipcode'] == user_from_list['address']['zipcode']
    assert user_data['company']['name'] == user_from_list['company']['name']
    assert user_data['company']['catchPhrase'] == user_from_list['company']['catchPhrase']
    assert user_data['company']['bs'] == user_from_list['company']['bs']

def test_user_data(api_users):
    response = api_users.get_all()
    users = response.json()
    for user in users:
        assert user['email'].count('@') == 1
        assert user['website']
        assert user['phone']
        assert isinstance(float(user["address"]["geo"]["lat"]), float)
        assert isinstance(float(user["address"]["geo"]["lng"]), float)


def get_users_data():
    with open("data/users.json") as file:
        data = json.load(file)
    return [ (item["user_id"], item["expected_status"]) for item in data ]

@pytest.mark.parametrize("user_id, expected_status", get_users_data())
def test_user_by_ids(api_users, user_id, expected_status):
    response = api_users.get_by_id(user_id)
    assert response.status_code == expected_status