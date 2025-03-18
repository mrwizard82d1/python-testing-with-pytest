from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

import cards


@pytest.fixture()
def cards_db():
    # The code **before** the `yield` statement is our test setup
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)

        # When the `yield` is executed, the test runs with `db` as its fixture
        print('Yielding to a test')
        yield db

        # The code **after** the `yield` statement is our test teardown. It is
        # guaranteed to run even if an Exception is raised by our test code.
        print('Closing the database')
        db.close()


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_exception(cards_db):
    raise Exception('Demonstrates clean up after test')
