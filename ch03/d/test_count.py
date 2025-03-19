# NOTE: We **do not** need to import `conftest.py`. The `conftest.py` 
# file is **automatically** read by pytest.


import cards


def test_empty(request, cards_db):
    print(request)
    assert cards_db.count() == 0


def test_two(request, cards_db):
    print(request)
    cards_db.add_card(cards.Card('first'))
    cards_db.add_card(cards.Card('second'))

    assert cards_db.count() == 2
