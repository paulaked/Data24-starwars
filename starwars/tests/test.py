import pytest
import starwars.config_manager as conf
import requests as rq
import starwars.app.starshipsAPI as sapi



REQ = rq.get(conf.SWAPI_URL, headers={'content-type': 'application/json'})
JSON = REQ.json()

'''
=====================================REQUESTS TESTS=========================================== 
'''


# This test checks the URL
def test_get_URL():
    assert conf.SWAPI_URL == "https://swapi.dev//api"


# This test checks the request status code (must be 200)
def test_check_request_code():
    assert REQ.status_code == 200


# This test checks if request returns an appropriate format
def test_get_request():
    test_dict = {'name': 'Tesla', 'engine': 'electric'}
    assert type(JSON) == type(test_dict)




'''
=====================================DATA EXTRACTION TESTS=========================================== 
'''

# This test checks the names of starships
def test_get_starships():
    count = 36
    list_length = len(sapi.get_starships(JSON['starships']))
    assert list_length == count


# This test checks the URLs of pilots
def test_get_pilots_URLS():
    starships = JSON["starships"]
    pilot_of_T1_URL = starships["pilots"]
    pilot_test_URL = "https//: ..."
    assert pilot_of_T1_URL == pilot_test_URL



