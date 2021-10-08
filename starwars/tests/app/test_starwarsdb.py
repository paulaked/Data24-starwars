from starwars.app.starwarsdb import StarWarsDB, pymongo

# An instance of a Star Wars Database to test
name = "StarWarsTEST"
db = StarWarsDB(db_name=name, overwrite=True)
client = pymongo.MongoClient()
starships = client[name]["Starships"]
characters = client[name]["Characters"]


def test_database_name():
    assert db.database_name == name


def test_insert():
    to_insert = {"name": "John Doe", "height": 170}
    # Insert via module method
    id = db.insert(into_collection=db.characters, data=to_insert)

    # Check insert via pymongo
    check = characters.find_one({"_id": id}, {})
    assert to_insert["name"] == check["name"]


def test_update():
    # Insert a document via pymongo
    ins_id = characters.insert_one({"name": "Jane Doe", "height": 165}).inserted_id

    # update the document via module method
    db.update(collection_name=db.characters, where={"_id": ins_id}, data={"height": 160})

    # Verify document has been updated
    check = characters.find_one({"_id": ins_id}, {})
    assert check["height"] == 160
