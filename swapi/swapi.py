import requests

# Depending on where the virtual environment is, the import path may be different:
try:
    from swapi import settings
except:
    import settings


def _get(resource_type, resource_id=""):
    url = f'{settings.BASE_URL}/{resource_type}/{resource_id}'  # e.g. BASE_URL/people/1 (Luke)
    return requests.get(url).json()


def get_starship(starship_id):
    return _get(settings.STARSHIPS, starship_id)


def get_character(character_id):
    return _get(settings.PEOPLE, character_id)


def get_all(resource_type):
    url = f'{settings.BASE_URL}/{resource_type}'  # The request may be returned in pages
    all_response = []  # A list containing all data

    while url:
        response = requests.get(url).json()
        all_response.extend(response['results'])

        url = response['next']  # The next request to make (next page)

    return all_response
