import starwars.app.requesting_sw as rqst
import unittest.mock as mock
import pytest


def test_API_call():
    assert rqst.sw.status_code == 200

def test_number_of_starships():
    assert rqst.count == len(rqst.sw_data)

