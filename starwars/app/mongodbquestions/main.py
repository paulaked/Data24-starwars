client = pymongo.MongoClient()
db = client['starwars']

luke = db.characters.find({"name":"Luke Skywalker"})

for names in luke:
    print(names)
droids = db.characters.find({"species.name": "Droid"})

for droid in droids:
    print(droid["name"])
# -------------------Q1:

vader = db.characters.find({"name": "Darth Vader"})

for info in vader:
    print(info['name'] + " " + str(info['height']))

# --------------------Q2:

yellow_eyes = db.characters.find({"eye_color": "yellow"})

for info in yellow_eyes:
    print(info['name'])
# --------------------Q3:

male_characters = db.characters.find({"gender": "male"})
collection.find({}, {}).limit(3)
counter = 0

while counter < 3:
    print(male_characters[counter]['name'])
    counter += 1
# --------------------Q4:

homeworld = db.characters.find({"species.name": "Human", "homeworld.name": "Alderaan"})

for names in homeworld:
    print(names["name"])
# --------------------Q5:

female_height = db.characters.find({"gender": "female"})
list = []
list2 = []
for info in female_height:
    if info["height"] != "unknown" or info["height"] is not None:
        list.append(info["height"])

print(list)
for numbers in list:
    if type(numbers) == int:
        list2.append(numbers)
print(list2)
print((sum(list2)) / (len(list)))

# --------------------Q6:
tallest = db.characters.find_one({}, {"_id": 0, "name": 1}, sort=[("height", pymongo.DESCENDING)])

print(tallest)
# tallest = db.characters.aggregate([{"$group": {"_id": "null", "max": {"$max": "$height"}}}])
tallest = db.characters.aggregate([{"$group": {"_id": 0, "max": {"$max": "$height"}}}])
heights = []

for info in tallest:
    if type(info["height"]) == int:
        heights.append(info["height"])
print(heights)
# print(max(heights))
