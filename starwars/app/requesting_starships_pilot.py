import starwars.config_manager as conf
import requests

"""
This function iterates through the starships in the API and returns their name as well as any information on the pilots
It takes into account the multiple pages to return a full list 

It iterates through the starships on the first page and returns all their names and associated pilots, 
once it has finished on the first page it moves onto the next one and continues this process until it reaches a page 
where the 'next' value is 'null' 
"""


def go_through_starships_name_pilots(api_link):
    response = requests.get(api_link)
    starships_result = response.json()
    for starship in starships_result['results']:
        yield starship['name'], starship['pilots']
    if 'next' in starships_result and starships_result['next'] is not None:
        next_page = go_through_starships_name_pilots(starships_result['next'])
        for page in next_page:
            yield page


list_of_starships_and_pilots = go_through_starships_name_pilots(conf.SWAPI_STARSHIPS_URL)
for ship in list_of_starships_and_pilots:
    print(ship)

