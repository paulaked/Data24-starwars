import starwars.config_manager as conf

import requests
import ast                          # Decoding the byte pulled from the API

first_pull = requests.get(conf.SWAPI_URL)
