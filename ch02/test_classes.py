import pytest

from cards import Card


class TestEquality:
    def test_equality(self):
        c1 = Card('something', 'larry', 'todo', 123)
        c2 = Card('something', 'larry', 'todo', 123)
        assert c1 == c2

    def test_equality_with_different_ids(self):
        c1 = Card('something', 'larry', 'todo', 123)
        c2 = Card('something', 'larry', 'todo', 456)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card('something', 'larry', 'todo', 123)
        c2 = Card('something', 'larry', 'done', 123)
