import pytest

import cards


def test_no_db_path_fail():
    cards.CardsDB()
