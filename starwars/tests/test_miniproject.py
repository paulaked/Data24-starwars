from starwars.app.miniproject import make_starship_dicts, add_to_list_of_ids
import pymongo


def test_make_starship_dicts():
    list_of_starship_dicts = make_starship_dicts()
    assert list_of_starship_dicts[1]["name"] == "CR90 corvette"


def test_add_to_list_of_ids():
    list_of_pilot_urls = ["https://swapi.dev/api/people/13/",
                          "https://swapi.dev/api/people/14/",
                          "https://swapi.dev/api/people/25/",
                          "https://swapi.dev/api/people/31/"]
    list_of_pilot_ids = []

    client = pymongo.MongoClient()  # Opens our pymongo server and assigns it to variable client
    db = client['starwars']

    list_of_pilot_ids = add_to_list_of_ids(list_of_pilot_urls, list_of_pilot_ids, db)

    assert 'ObjectId' in list_of_pilot_ids[3]
