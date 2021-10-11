from starwars.app.miniproject import make_starship_dicts, add_to_list_of_ids
import pymongo


def test_make_starship_dicts():  # This checks that the name of the first starship dictionary from the list getting
    #                              returned by make_starship_dicts is CR90 corvette, as it should be
    list_of_starship_dicts = make_starship_dicts()
    assert list_of_starship_dicts[0]["name"] == "CR90 corvette"


def test_add_to_list_of_ids():
    list_of_pilot_urls = ["https://swapi.dev/api/people/13/",
                          "https://swapi.dev/api/people/14/",
                          "https://swapi.dev/api/people/25/",
                          "https://swapi.dev/api/people/31/"]
    list_of_pilot_ids = []  # Creates two variables to be passed to the add_to_list_of_ids function
    # The first is a list of 4 pilot urls: links to the API
    # The second is the empty list of pilot IDs

    client = pymongo.MongoClient()  # Opens our pymongo server and assigns it to variable client
    db = client['starwars']  # Assigns the 'starwars' database to the variable db, to be passed to the function

    # The function is passed the 3 arguments, and should return a list of pilot IDs
    list_of_pilot_ids = add_to_list_of_ids(list_of_pilot_urls, list_of_pilot_ids, db)
    # We check that the 4th element in the list has Nien Nunb's ObjectID
    assert '615dbd1cb9ea613cfac2f0c8' in str(list_of_pilot_ids[3])
