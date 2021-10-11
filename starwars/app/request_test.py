import pytest
import starwars.config_manager as conf
import requests as rq

#uses requests package to pull data from the API
request_url = rq.get(f'{conf.SWAPI_URL}/api/starships', headers={'content-type': 'application/json'})
data = requests.get(url)
JSON_Data = info.json()
#print(data)

#uses pytest to ensure status code is 200
def request_code_check():
    assert info.status_code==200

#tests starship's name
def test_starship_name():
    starship = JSON_Data["starships"][1]
    assert starship == "CR90 corvette"

#print(test_starship_name())