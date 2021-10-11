import starwars.app.requesting_sw as rqst
import unittest.mock as mock
import pytest


def test_API_call():
    assert rqst.requests_data_from_url().status_code == 200


def test_number_of_starships_called():
    assert len(rqst.list_of_all_ships()) == 36


def test_if_dictionary():
    assert type(rqst.converting_ship_names_to_dict()) == dict


def test_number_of_pilots():
    assert rqst.combine_ship_name_pilot_name()["TIE Advanced x1"] == ["Darth Vader"]


# Need to test the length of the output expecting 36?

def test_if_combined_list_is_correct_length():
    assert len(rqst.combine_ship_name_pilot_name()) == 36


# Check to see if pilot is in dictionary.

def test_ship_doesnt_have_pilot():
    assert rqst.combine_ship_name_pilot_name()["Death Star"] == []


# Check to see correct objectId for a given pilot.

def test_ship_name_pilot_id():
    assert rqst.complete_ship_information_with_pilot_ids()['TIE Advanced x1']['pilots'] \
           == ["ObjectID:615d754d6d19bc77fdfda7a9"]


# Check to see when multiple pilots fly one star ship that the correct number of objects id's are produced.

def test_pilot_id_length():
    assert len(rqst.complete_ship_information_with_pilot_ids()['Millennium Falcon']['pilots']) == 4
