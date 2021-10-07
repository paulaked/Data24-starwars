import starwars.config_manager as conf
import requests
import json
from pprint import pprint

starships = requests.get(conf.SWAPI_URL+"/api/starships")
starships_list = starships.json()["results"]
# pprint(starships_list)
