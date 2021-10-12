import pymongo
from pprint import pprint

print("Start: Test Script")
from swapi import swapi as api

db_name = "AhmedsStarWarsDB"
client = pymongo.MongoClient()
db = client[db_name]
starships = db["Starships"]
# characters = db["Characters"]
characters = pymongo.MongoClient()[db_name]["Characters"]

millennium_falcon = starships.find_one({"name": "Millennium Falcon"}, {"_id": 0, "pilots": 1})
model = "YT-1300 light freighter"

# Now loop through URLS and create reference
pilots = list()
for url in millennium_falcon['pilots']:
    pilot = api.extract_from_url(url)  # Get the pilot data
    pilot = characters.find_one({"name": pilot["name"]}, {"_id": 1})  # Find this pilot in Characters collection
    pilots.append(pilot['_id'])  # Replace url with reference


# Update the Starship.pilots field with references instead of urls:
starships.update_one(
    {"name": "Millennium Falcon"},
    {"$set": {"pilots": pilots}}
)

# pprint(pilots)
print("End")