import requests
from jsonschema import validate
from schemas.users import get_users, post_users, put_users


def test_get_users(base_url):
    url = base_url + '/api/users'

    response = requests.get(url, params='page=2')

    assert response.status_code == 200

    response_json_body = response.json()
    validate(response_json_body, get_users)


def test_create_users(base_url):
    url = base_url + '/api/users'
    body = {
        "name": "alex",
        "job": "qa"
    }
    response = requests.post(url, data=body)
    assert response.status_code == 201
    response_json_body = response.json()
    validate(response_json_body, post_users)


def test_change_users(base_url):
    url = base_url + '/api/users/2'
    body = {
        "name": "alex",
        "job": "qa"
    }
    response = requests.put(url, data=body)
    assert response.status_code == 200
    response_json_body = response.json()
    validate(response_json_body, put_users)


def test_delete_users(base_url):
    url = base_url + '/api/users/2'

    response = requests.delete(url)
    assert response.status_code == 204
    assert response.text == ''


def test_user_not_found(base_url):
    url = base_url + '/api/users/23'

    response = requests.get(url)

    assert response.status_code == 404
