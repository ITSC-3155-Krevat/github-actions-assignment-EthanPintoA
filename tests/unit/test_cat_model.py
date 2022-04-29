from src.models import Cat


def test_cat_model():
    cat = Cat('Piero', 'Orange', 4)

    assert cat.name == 'Piero'
    assert cat.breed == 'Orange'
    assert cat.num_legs == 4
