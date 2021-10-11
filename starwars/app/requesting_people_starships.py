import starwars.config_manager as conf
import requests

"""
This function iterates through the people and returns their name as well as the url of the starship(s) they pilot 
It takes into account the next page link in the API

It iterates through the people on the first page and returns all their names and the starship(s) url, 
once it has finished on the first page it moves onto the next one and continues this process until it reaches a page 
where the 'next' value is 'null'
"""


def go_through_people_name_starships(api_link):
    response = requests.get(api_link)
    people_result = response.json()
    for people in people_result['results']:
        yield people['name'], people['starships']
    if 'next' in people_result and people_result['next'] is not None:
        next_page = go_through_people_name_starships(people_result['next'])
        for page in next_page:
            yield page


list_of_people = go_through_people_name_starships(conf.SWAPI_PEOPLE_URL)
for character in list_of_people:
    print(character)

