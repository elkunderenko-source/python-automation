def test_users_api(api_users):
    response = api_users.get_users()
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
    response = api_users.get_users()
    users = response.json()
    for user in users:
        if user['username'] == "Bret":
            user_from_list = user
            break

    user_data = api_users.get_user_by_id(user_from_list["id"]).json()
    assert user_data['username'] == user_from_list['username']
    assert user_data['address']['street'] == user_from_list['address']['street']
    assert user_data['address']['suite'] == user_from_list['address']['suite']
    assert user_data['address']['city'] == user_from_list['address']['city']
    assert user_data['address']['zipcode'] == user_from_list['address']['zipcode']
    assert user_data['company']['name'] == user_from_list['company']['name']
    assert user_data['company']['catchPhrase'] == user_from_list['company']['catchPhrase']
    assert user_data['company']['bs'] == user_from_list['company']['bs']

def test_user_data(api_users):
    response = api_users.get_users()
    users = response.json()
    for user in users:
        assert user['email'].count('@') == 1
        assert user['website']
        assert user['phone']
        assert isinstance(float(user["address"]["geo"]["lat"]), float)
        assert isinstance(float(user["address"]["geo"]["lng"]), float)
