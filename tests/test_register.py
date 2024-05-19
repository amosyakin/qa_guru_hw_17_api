import requests
from jsonschema import validate
from schemas.register import post_register


base_url = "https://reqres.in"


def test_user_register():
    url = base_url + '/api/register'
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(url, data=body)
    assert response.status_code == 200
    response_json_body = response.json()
    validate(response_json_body, post_register)


def test_user_register_without_password():
    url = base_url + '/api/register'
    body = {
        "email": "eve.holt@reqres.in"
    }
    response = requests.post(url, data=body)
    assert response.status_code == 400
    response_json_body = response.json()
    assert response_json_body['error'] == "Missing password"


def test_user_register_without_email():
    url = base_url + '/api/register'
    body = {
        "password": "pistol"
    }
    response = requests.post(url, data=body)
    assert response.status_code == 400
    response_json_body = response.json()
    assert response_json_body['error'] == "Missing email or username"


def test_user_register_with_empty_body():
    url = base_url + '/api/register'
    body = {

    }
    response = requests.post(url, data=body)
    assert response.status_code == 400
    response_json_body = response.json()
    assert response_json_body['error'] == "Missing email or username"
