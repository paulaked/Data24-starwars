from starwars.app.create_starships import create_starships


def test_create_starships():
    test_value = create_starships()
    assert test_value == "working"
