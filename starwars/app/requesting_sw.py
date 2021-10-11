import starwars.config_manager as conf
import requests

sw = requests.get(conf.SWAPI_URL)
star_wars_data = sw.json()
print(star_wars_data)