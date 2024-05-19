import pytest


@pytest.fixture(scope='function')
def base_url():
    return "https://reqres.in"
