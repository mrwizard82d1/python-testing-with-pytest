from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

import cards


@pytest.fixture(scope='session')
def cards_db():
    """CardsDB object conneected to a temporary database."""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)

        yield db

        db.close()
