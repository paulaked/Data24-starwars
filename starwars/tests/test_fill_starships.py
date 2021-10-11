from starwars.app.fill_starships import fill_starships


def test_fill_starships():
    test_value = fill_starships()
    assert test_value == "3500000"
