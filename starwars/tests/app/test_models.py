from starwars.app.models import (
    BaseModel,
    Character,
    Starship
)


def test_base_model_get():
    data = {'Name': 'John', 'Height': 180, 'Weight': 200}
    base_model = BaseModel(data)
    to_retrieve = ['Name', 'Weight']
    base_model.get(to_retrieve)
    expected = {'Name': 'John', 'Weight': 200}
    assert base_model.get(to_retrieve) == expected



def test_character_class_starship():
    pass


def test_starship_class_pilots():
    pass
