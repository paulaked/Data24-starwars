import starwars.config_manager as conf
import requests


def go_through_people():
    people_result = requests.get(conf.SWAPI_PEOPLE_URL).json()
    for character in people_result['results']:
        yield character['name']


list_of_people = go_through_people()
for people in list_of_people:
    print(people)