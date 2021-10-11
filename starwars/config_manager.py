from definitions import PROJECT_ROOT_DIR
import configparser
import os

_config = configparser.ConfigParser()

_config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))

SWAPI_URL = _config['default']['url']
SWAPI_STARSHIPS_MILLENNIUM_FALCON_URL = _config['default']['url2']
SWAPI_PEOPLE_URL = _config['default']['url3']
SWAPI_STARSHIPS_URL = _config['default']['url4']

