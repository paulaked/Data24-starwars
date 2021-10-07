# This file tests the functions from the code
import pytest
import starwars.app.GetFullSWInfo as GetFullSWInfo
import starwars.app.GetPilotName as GetPilotName
import starwars.app.GetID as GetID


def test_generate_list_of_ships_with_pilot_apis():
    assert GetFullSWInfo.generate_list_of_ships_with_pilot_apis([{"name": "test_ship",
                                                                 "pilots":
                                                        ["pilot1", "pilot2", "pilot3"]}]) \
           == ["test_ship", ["pilot1", "pilot2", "pilot3"]]


def test_get_pilot_name():
    assert GetPilotName.get_pilot_name("https://swapi.dev/api/people/13/") == "Chewbacca"

# 615d755b10819e26561053bc
def test_getID():
    assert str(GetID.get_ID("Chewbacca")["_id"]) == "615d755b10819e26561053bc"