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
