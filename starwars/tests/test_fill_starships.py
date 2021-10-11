from starwars.app.fill_starships import fill_starships


def test_fill_starships():
    test_value = fill_starships()
    assert test_value == "3500000"  # Checking to see if the cost_in_credits of the CR90 corvette is 3500000
