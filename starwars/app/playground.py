import starwars.config_manager as conf
import requests


def go_through_people_name_starships(api_link):
    response = requests.get(api_link)
    people_result = response.json()
    for people in people_result['results']:
        if people['starships'] == []:
            pass
        else:
            yield people['name'], people['starships']
    if 'next' in people_result and people_result['next'] is not None:
        next_page = go_through_people_name_starships(people_result['next'])
        for page in next_page:
            yield page


list_of_people_and_starships = go_through_people_name_starships(conf.SWAPI_PEOPLE_URL)
for character in list_of_people_and_starships:
    print(character)

