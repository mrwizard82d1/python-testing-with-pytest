import pytest

from cards import Card


def test_with_fail():
    c1 = Card('sit there', 'larry')
    c2 = Card('do something', 'leslie')
    if c1 != c2:
        pytest.fail("they don't matcrh")
