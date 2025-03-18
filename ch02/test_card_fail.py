from cards import Card


def test_equality_fail():
    c1 = Card('sit there', 'larry')
    c2 = Card('do something', 'leslie')
    assert c1 == c2
