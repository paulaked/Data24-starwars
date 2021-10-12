import pymongo

# Depending on where the virtual environment is, the import path may be different:
try:
    from starwars.app.settings import COLLECTIONS
except:
    from settings import COLLECTIONS


class StarWarsDB:
    def __init__(self, db_name="StarWars", overwrite=True):
        self.__db_name = db_name
        self.__client = pymongo.MongoClient()
        self.__db = self.__client[db_name]

        self.__collections = dict()
        for v in vars(COLLECTIONS).values():
            self.__collections[v] = self.__db[v]

        if overwrite:
            self.__client.drop_database(self.__db)

    @property
    def database_name(self):
        # return self.__db._Database__name
        return self.__db_name

    def __query(self, query):
        pass

    def insert(self, collection, data: dict):
        return self.__collections[collection].insert_one(data).inserted_id

    def update(self, collection, where, data):
        return self.__collections[collection].update_one(where, {"$set": data})

