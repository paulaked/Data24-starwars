import starwars.app.requesting_sw as rqst
import unittest.mock as mock
import pytest


def test_API_call():
    assert rqst.requests_data_from_url().status_code == 200


def test_number_of_starships_called():
    assert rqst.number_of_ships() == len(rqst.list_of_all_ships())


def test_if_dictionary():
    assert type(rqst.converting_shipnames_to_dict()) == dict

# def test_check_if_all_ships_present():
#     assert

# Need a test to check correct number of pilots.
# Need a test to check correct number of ships in json files.
# Need a test to see if a random pilot name matches with random star ship.
# Need to test the length of the ouput expecting 36?
