import starwars.config_manager as conf
import starwars.app.API_Pulling as pulling
import starwars.app.Pilot_Interaction as pilot

import requests
import django.core.validators as valids

test_interactor = pulling.ShipInfo()
test_pilot_holder = pilot.PilotInteraction()
url_validator = valids.URLValidator()


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


def test_pilot_puller():
    test_pilot = test_pilot_holder.pull_single_pilot("https://swapi.dev/api/people/1")
    assert test_pilot["name"] == "Luke Skywalker"

def test_first_dictionary():
    test_dict_one = test_pilot_holder.get_url_dict
    test_list_one = list(test_dict_one.values())
    assert url_validator(test_list_one[0][0]) is True

def test_second_dictionary():
    test_dict_two = test_pilot_holder.get_name_dict
    test_list_two = list(test_dict_two.values())
    pass

def test_third_dictionary():
    test_dict_three = test_pilot_holder.get_object_dict
    test_list_three = list(test_dict_three.values())
    assert True