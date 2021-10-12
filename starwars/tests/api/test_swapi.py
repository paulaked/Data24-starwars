from swapi import swapi as api


def test_get():
    assert api._get(api.settings.CHARACTER, 1)['name'] == "Luke Skywalker"
    assert api._get(api.settings.STARSHIPS, 10)['name'] == "Millennium Falcon"


def test_get_starship():
    assert api.get_starship(2)['name'] == "CR90 corvette"


def test_get_character():
    assert api.get_character(20)['name'] == "Yoda"


def test_get_all():
    assert len(api.get_all(api.settings.CHARACTER)) == 82


def test_extract_from_url():
    character = api.extract_from_url(url="https://swapi.dev/api/people/15")
    assert character['name'] == "Greedo"


def test_extract_from_urls():
    urls = ["https://swapi.dev/api/people/5", "https://swapi.dev/api/starships/9"]
    names_returned = [c['name'] for c in api.extract_from_urls(urls)]  # Capture the 'name' field from returned list
    assert all(name in names_returned for name in ["Leia Organa", "Death Star"])
