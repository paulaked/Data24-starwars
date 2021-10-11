
from file1 import *


def test_starships_name():
    assert get_info(2, 'name', 'starships') == 'CR90 corvette'


def test_secondary_number():
    assert secondary_number_list(10, 'starships', 'pilots') == ['13', '14', '25', '31']


def test_pilot_names():
    assert get_pilot(10) == ['Chewbacca', 'Han Solo', 'Lando Calrissian', 'Nien Nunb']


def test_pilot_object_ids():
    assert get_pilot_object_ids(10) == ['615e9e15458d51eeea1431e9',
                                        '615e9e200e1c7d4e755766d2',
                                        '615e9e27e643b2379ddc2b8a',
                                        '615e9e2cfc8b367d393967b0']

