import requests as requests


def test_get_response_for_website_check_status_code_equals_200():
    response = requests.get("https://swapi.dev")
    assert response.status_code == 200


def test_get_starship_check_name_equals_millennium_falcon_():
    response = requests.get("https://swapi.dev/api/starships/10/")
    response_body = response.json()
    assert response_body["name"] == "Millennium Falcon"
