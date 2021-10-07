import requests as requests


def test_get_response_for_website_check_status_code_equals_200():
    response = requests.get("https://swapi.dev")
    assert response.status_code == 200

