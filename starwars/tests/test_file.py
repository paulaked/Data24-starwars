import starwars.app.requesting_sw as rqst
import unittest.mock as mock
import pytest


def test_API_call():
    assert rqst.Requests_Data_From_URL().status_code == 200


def test_number_of_starships():
    assert rqst.number_of_ships() == len(rqst.list_of_all_ships())
