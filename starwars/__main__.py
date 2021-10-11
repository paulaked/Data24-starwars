import ExtractShipAndPilotAPIs
import requesting_sw
import starwars.app.ExtractShipAndPilotAPIs as ExtractShipAndPilotApis
import starwars.app.GetPilotName as GetPilotName
import starwars.app.GetID as GetID
import starwars.app.ReplaceAPIsWithIDs as ReplaceAPIsWithIDs
import pymongo
from pprint import pprint

# start with GetFullSWInfo
# for each element in list:
#   input Pilot API into GetPilot to get the name
#   use this name to search database for ID
#   Add entry into starships collection in MongoDB


if __name__ == '__main__':
    # connect to mongo db 'starwars'
    client = pymongo.MongoClient()
    db = client['starwars']
    # delete existing documents
    db.starships.delete_many({})
    # API call to get json of ship info and loop through them - Ship is a dictionary
    for ship in requesting_sw.starships_list:
        # get the ship and pilot apis from the dictionary -> [name, [api1, api2,...]]
        ship_name_and_apis = ExtractShipAndPilotAPIs.extract_ship_pilot_and_apis(ship)
        # Here we have two cases. If the ship has at least 1 pilot and if it has no pilots
        if len(ship_name_and_apis[1]) > 0:
            # this list is initialised each time as it will hold the id strings
            id_codes = []
            # for each API string do the following
            for api in ship_name_and_apis[1]:
                # use the API to get the pilot name
                name = GetPilotName.get_pilot_name(api)
                # use the name to get the id from mongo db and append to list
                id_codes.append(GetID.get_ID(name)['_id'])
            # changes the list of apis with the list of id's
            updated_ship = ReplaceAPIsWithIDs.replace_apis_with_ids(ship, id_codes)
            # inserts into collection
            db.starships.insert_one(updated_ship)
        else:
            # nothing to change here so insert into collection
            db.starships.insert_one(ship)



# for testing
# for i in db.starships.find({'name': 'Millennium Falcon'}):
#     print(i)
