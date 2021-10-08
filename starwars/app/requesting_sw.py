import starwars.config_manager as conf
import requests
from pprint import pprint

sw = requests.get(conf.SWAPI_URL)

# print(sw)


# x = requests.get(f'{conf.SWAPI_URL}/starships/2?format=json')
x = requests.get(f'{conf.SWAPI_URL}/starships/2').json()
# pprint(x)
# print(x['name'])


x = requests.get(f'{conf.SWAPI_URL}/starships/2?format=json')
pprint(type(x))


