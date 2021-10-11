import starwars.config_manager as conf
import requests

"""
This function iterates through the people in the Star Wars API and returns their name
UPDATE:
    -> there are multiple pages for people (9 pages)
    -> this function only lists from the first page
"""
# def go_through_people():
#     people_result = requests.get(conf.SWAPI_PEOPLE_URL).json()
#     for character in people_result['results']:
#         yield character['name']
#
#
# list_of_people = go_through_people()
# for people in list_of_people:
#     print(people)



"""
This function builds on the previous one, it still iterates through the people and returns their name but takes into
account the next page link in the API

It iterates through the people on the first page and returns all their names, once it has finished on the first page
it moves onto the next one and continues this process until it reaches a page where the 'next' value is 'null' 
"""


def go_through_people(api_link):
    response = requests.get(api_link)
    people_result = response.json()
    for character in people_result['results']:
        yield character['name']
    if 'next' in people_result and people_result['next'] is not None:
        next_page = go_through_people(people_result['next'])
        for page in next_page:
            yield page


list_of_people = go_through_people(conf.SWAPI_PEOPLE_URL)
for people in list_of_people:
    print(people)
