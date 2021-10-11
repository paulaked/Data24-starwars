import starwars.config_manager as conf
import starwars.app.API_Pulling as pulling
import starwars.app.Pilot_Interaction as pilot
import starwars.app.Mongo_Interaction as mongo

import requests
import pymongo

db_name = "starwars"
collection_name = "starships"

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


test_pilot_holder = pilot.PilotInteraction(db_name)


def test_pilot_puller():
    test_pilot = test_pilot_holder.pull_single_pilot("https://swapi.dev/api/people/1")
    assert test_pilot["name"] == "Luke Skywalker"


def test_first_dictionary():
    test_dict_one = test_pilot_holder.get_url_dict
    test_list_one = list(test_dict_one.values())
    assert test_list_one[0][0].startswith("https://swapi.dev/api/")


def test_second_dictionary():
    test_dict_two = test_pilot_holder.get_name_dict
    test_list_two = list(test_dict_two.values())
    assert type(test_list_two[0][0]) == str


def test_third_dictionary():
    test_dict_three = test_pilot_holder.get_object_dict
    test_list_three = list(test_dict_three.values())
    assert type(test_list_three[0][0]) == str


test_mongo_file = mongo.Mongo(db_name)


def test_key_puller():
    keylist = test_mongo_file.get_ship_keys
    assert type(keylist) == list and type(keylist[0]) == str












