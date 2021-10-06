import starwars.config_manager as conf
import requests

sw = requests.get(conf.SWAPI_URL)

print(sw)