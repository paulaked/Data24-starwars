import starwars.config_manager as conf
import requests
import json


# This connect with conf.SWAPI_URL by requests package
# Catches 2 errors: ConnectionError & JSONDecodeError
# Returns False if fail
# Returns JSON file is success
def get_request():
    starwars_Data = None
    try:
        # convert to JSON file
        starwars_Data = requests.get(f'{conf.SWAPI_URL}/api/starships', headers={'content-type': 'application/json'}).json()
    except requests.exceptions.ConnectionError as CE:
        print(CE)
    except json.decoder.JSONDecodeError as JSONError:
        print(f"Decoder problem (check the URL): {JSONError}")
    if starwars_Data:
        return starwars_Data
    else:
        return False


