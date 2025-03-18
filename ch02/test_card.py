from cards import Card

def test_field_access():
    c = Card('something', 'larry', 'todo', 123)
    assert c.summary == 'something'
    assert c.owner == 'larry'
    assert c.state == 'todo'
    assert c.id == 123


def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == 'todo'
    assert c.id is None


def test_equality():
    c1 = Card('something', 'larry', 'todo', 123)
    c2 = Card('something', 'larry', 'todo', 123)
    assert c1 == c2


def test_equality_with_different_ids():
    c1 = Card('something', 'larry', 'todo', 123)
    c2 = Card('something', 'larry', 'todo', 124)
    assert c1 == c2


def test_inequality():
    c1 = Card('now for something', 'larry', 'todo', 123)
    c2 = Card('completely different', 'leslie', 'done', 123)

    assert c1 != c2

def test_from_dict():
    c1 = Card('something', 'larry', 'todo', 123)
    c2_dict = {
        'summary': 'something',
        'owner': 'larry',
        'state': 'todo',
        'id': 123,
    }
    c2_expected = Card.from_dict(c2_dict)
    assert c1 == c2_expected


def test_to_dict():
    c1 = Card('something', 'larry', 'todo', 123)
    c2 = c1.to_dict()
    c2_expected = {
        'summary': 'something',
        'owner': 'larry',
        'state': 'todo',
        'id': 123,
    }
    assert c2 == c2_expected
