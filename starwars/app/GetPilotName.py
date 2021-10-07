import requests
import json
from pprint import pprint


# function which takes in a person API URL and returns the individuals name
def get_pilot_name(api_url):
    pilot_info = requests.get(api_url)
    return pilot_info.json()["name"]