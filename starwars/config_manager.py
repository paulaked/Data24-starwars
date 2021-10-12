from definitions import PROJECT_ROOT_DIR
import configparser
import os
import pytest

_config = configparser.ConfigParser()

_config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))

SWAPI_URL = _config['default']['url']
DEFAULT_DB_NAME = _config['default']['db_name']
