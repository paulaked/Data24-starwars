import starwars.config_manager as conf
import starwars.app.API_Pulling as pulling

import requests

test_interactor = pulling.ShipInfo()

def test_api_connection():
    test_pull = requests.get(conf.SWAPI_URL)
    assert test_pull.status_code == 200


def test_ship_pull_found():
    ship = test_interactor.pull_single_ship(2)
    assert ship["name"] == "CR90 corvette"


def test_ship_not_found():
    ship = test_interactor.pull_single_ship(1)
    assert ship == f"Object with url number {int(1)} not found."


def test_to_dictionary():
    assert type(test_interactor.convert_to_dict(requests.get(conf.SWAPI_URL+"/starships/2"))) == dict


def test_pull_ship_count():
    assert test_interactor.pull_ship_count() == 36


def test_pull_all_ships():
    result_from_pulling_everything = test_interactor.pull_all_ships()
    assert type(result_from_pulling_everything) == list \
           and len(result_from_pulling_everything) == test_interactor.pull_ship_count()

