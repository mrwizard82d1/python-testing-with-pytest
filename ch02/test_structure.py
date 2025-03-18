import pytest

from cards import Card


def test_to_dict():
    # Given a Card object with known contents
    c1 = Card('something', 'larry', 'todo', 123)

    # When we call `to_dict()` on the object
    c2 = c1.to_dict()

    # Then the result will be a dictionary with known content
    c2_expected = {
        'summary': 'something',
        'owner': 'larry',
        'state': 'todo',
        'id': 123,
    }
    assert c2 == c2_expected
