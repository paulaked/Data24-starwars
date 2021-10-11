import pymongo

client=pymongo.MongoClient()

db=client["StarWars"]

Character_det = db.characters.find_one({"name":"Darth Vader"}, {"_id": 1, "height": 1, "name": 1})
print(Character_det)
print(Character_det["_id"]) == ['615e9e15458d51eeea1431e9','615e9e200e1c7d4e755766d2','615e9e27e643b2379ddc2b8a','615e9e2cfc8b367d393967b0']