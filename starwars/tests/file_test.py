from file1 import *
from bson import ObjectId  # Used to test if the correct inputs are collected from StarWars database.


def test_starships_name():
    assert get_info(2, 'name', 'starships') == 'CR90 corvette'


def test_secondary_number():
    assert secondary_number_list(10, 'starships', 'pilots') == ['13', '14', '25', '31']


def test_pilot_names():
    assert get_pilot(10) == ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb']


def test_pilot_object_ids():
    assert get_pilot_object_ids(10) == [ObjectId('61648c1de2b4c67b016f2b51'),
                                        ObjectId('61648c287fe84354f27559a2'),
                                        ObjectId('61648c2ff5d2d6fc8683b6d6'),
                                        ObjectId('61648c347109080275dec2e7')]


def test_check_collection():
    assert check_collection('StarWars',
                            'starships',
                            'Millennium Falcon'
                            ) == {'pilots': [ObjectId('61648c1de2b4c67b016f2b51'),
                                             ObjectId('61648c287fe84354f27559a2'),
                                             ObjectId('61648c2ff5d2d6fc8683b6d6'),
                                             ObjectId('61648c347109080275dec2e7')],
                                  'starship': 'Millennium Falcon'}
