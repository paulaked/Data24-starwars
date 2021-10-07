import starwars.app.requesting_sw as rqst
import unittest.mock as mock
import pytest


def test_API_call():
    assert rqst.requests_data_from_url().status_code == 200


def test_number_of_starships():
    assert rqst.number_of_ships() == len(rqst.list_of_all_ships())


def test_if_dictionary():
    assert type(rqst.converting_shipnaes_to_dict()) == dict