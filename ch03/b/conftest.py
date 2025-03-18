from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

import cards


@pytest.fixture(scope='session')
def db():
    """CardsDB object conneected to a temporary database."""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)

        yield db_

        db_.close()


# Since this fixture depends on `db`, the **previous** fixture, we ensure
# that we run `db` and **then** run this fixture which deletes any records
# in the (temporary) database.
@pytest.fixture(scope='function')
def cards_db(db):
    """CardsDB object that's empty."""
    db.delete_all()
    return db
