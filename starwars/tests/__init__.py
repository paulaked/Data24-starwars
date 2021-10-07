import pytest
import starwars.config_manager as conf


def test_get_URL():
    assert conf.SWAPI_URL == "https://swapi.dev"
