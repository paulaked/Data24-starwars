from file1 import *

# Database = 'StarWars'
# Collection = 'starships'
#
# create_collection(Database, Collection)
#
# for i in range(100):
#     try:
#
#         starship = get_info(i, 'name', 'starships')
#         pilot = get_pilot_object_ids(i)
#         add_starship_document(Database, Collection, starship, pilot)
#
#     except Exception:
#
#         pass

client = pymongo.MongoClient()
db = client['StarWars']
db.get_collection('starships').find(
        {'starship': "Millennium Falcon"}
        )