import unittest
import swapi
import request_test

class API_TESTS(unittest.TestCase):

    def people_count_test(self):
        people = swapi.get_all('people')
        self.assertEquals(people.count(), 87)
        self.assertEquals('<PeopleQuerySet - 87>', people.__repr__())

    def get_tests(self):
        starship = swapi.get_starship(3)
        self.assertEquals('<Starship - Star Destroyer>', starship.__repr__())
        vehicle = swapi.get_vehicle(4)
        self.assertEquals('<Vehicle - Sand Crawler>', vehicle.__repr__())
        species = swapi.get_species(1)
        self.assertEquals('<Species - Human>', species.__repr__())
        film = swapi.get_film(1)
        self.assertEquals('<Film - A New Hope>', film.__repr__())
        planet = swapi.get_planet(1)
        self.assertEquals('<Planet - Tatooine>', planet.__repr__())

    def test_get_person(self):
        Luke = swapi.get_person(1)
        self.assertEquals(Luke.name, "Luke Skywalker")
        self.assertEquals(
            '<Person - Luke Skywalker>', Luke.__repr__())