import starwars.config_manager as conf
import requests


def go_through_starships(api_link):
    response = requests.get(api_link)
    starships_result = response.json()
    for starship in starships_result['results']:
        yield starship['name']
    if 'next' in starships_result and starships_result['next'] is not None:
        next_page = go_through_starships(starships_result['next'])
        for page in next_page:
            yield page


list_of_starships = go_through_starships(conf.SWAPI_STARSHIPS_URL)
for ship in list_of_starships:
    print(ship)

