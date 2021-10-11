# This file tests the functions from the code
import pytest
import starwars.app.ExtractShipAndPilotAPIs as ExtractShipAndPilotApis
import starwars.app.GetPilotName as GetPilotName
import starwars.app.GetID as GetID
import starwars.app.ReplaceAPIsWithIDs as ReplaceAPIsWithIDs


def test_extract_ship_pilot_and_name():
    assert ExtractShipAndPilotApis.extract_ship_pilot_and_apis({"name": "test_ship",
                                                                 "pilots":
                                                        ["pilot1", "pilot2", "pilot3"]}) \
           == ["test_ship", ["pilot1", "pilot2", "pilot3"]]


def test_get_pilot_name():
    assert GetPilotName.get_pilot_name("https://swapi.dev/api/people/13/") == "Chewbacca"


def test_get_id():
    assert str(GetID.get_ID("Chewbacca")["_id"]) == "615d755b10819e26561053bc"


def test_replace_apis_with_ids():
    assert ReplaceAPIsWithIDs.replace_apis_with_ids({"pilots": []}, ["1", "2", "3"]) ==\
           {"pilots": ["1", "2", "3"]}
