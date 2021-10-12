from starwars.app.scripts.generate_database import (
    create_database,
    get_all_characters,
    get_all_starships
)
from starwars.app.starwarsdb import StarWarsDB
import pymongo

# An instance of a Star Wars Database to test
db_name = "StarWarsDBGeneratorTest"
client = pymongo.MongoClient()
db = client[db_name]
starships = client[db_name]["Starships"]
characters = client[db_name]["Characters"]


def test_create_database():
    test_db = create_database(db_name=db_name)
    assert isinstance(test_db, StarWarsDB)  # Check if the return type is correct
    assert test_db.database_name == db_name  # Check if module code named database correctly

    # Using PyMongo to access the database directly, check if database is populated correctly:
    assert db_name in client.list_database_names()  # Check if the database exists
    assert all(coll in db.list_collection_names() for coll in ['Characters', 'Starships'])  # Check if collecitons exist
    assert characters.count_documents({}) == 82  # Check if # documents in characters collection is correct
    assert starships.count_documents({}) == 36  # Check if # documents in starships collection is correct


def test_get_all_characters():
    character_list = get_all_characters()

    # First check if all characters are returned
    assert len(character_list) == 82

    # Then ensure that a few known characters are in the returned list
    character_names = [c['name'] for c in character_list]  # Capture all character names returned
    check_for = ["Luke Skywalker", "Anakin Skywalker", "Boba Fett", "Qui-Gon Jinn", "Darth Maul", "Jango Fett"]
    assert all(person in character_names for person in check_for)  # Check if all the people above have been returned


def test_get_all_starships():
    starship_list = get_all_starships()

    # First check if all starships are returned
    assert len(starship_list) == 36

    # Then ensure that the following starships are in the returned list
    starship_names = [c['name'] for c in starship_list]  # Capture all starship names returned
    check_for = ["CR90 corvette", "A-wing", "Scimitar", "V-wing"]
    assert all(ship in starship_names for ship in check_for)  # Check if all the people above have been returned
