import pymongo


class StarWarsDB:
    def __init__(self, db_name="StarWars", overwrite=True):
        self.__db_name = db_name
        self.__client = pymongo.MongoClient()
        self.__db = self.__client[db_name]
        self.__collections = {
            "Starships": self.__db.Starships,
            "Characters": self.__db.Characters
        }

        if overwrite:
            self.__client.drop_database(self.__db)

    @property
    def database_name(self):
        # return self.__db._Database__name
        return self.__db_name

    @property
    def collections(self):
        return self.__collections.copy()

    @property
    def starships(self):
        return "Starships"  # Getter only, this value should never be changed

    @property
    def characters(self):
        return "Characters"  # Getter only, this value should never be changed

    def __query(self):
        pass

    def insert(self, into_collection, data):
        pass

    def update(self, collection_name, where, data):
        pass