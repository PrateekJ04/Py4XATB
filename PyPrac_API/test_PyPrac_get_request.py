import pytest
import requests


@pytest.mark.smoke
def test_get_request():
    response = requests.get("https://reqres.in/api/users?page=2")
    response_status = response.status_code
    assert response_status == 200
