from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

import cards
    

def pytest_addoption(parser, pluginmanager):
    """
    Allows `pytest` to use the additional command line option, '--func-db'.
    """
    parser.addoption(
        '--func-db',
        action='store_true',
        default=False,
        help='Use a new database instance for each test.'
    )


def db_scope(fixture_name, config):
    """
    Allows a user to specify the scope of a `pytest.fixture` by 
    specifying a command line argument. 
    
    If a user includes the command line argument, '--func-db', 
    the test database will have "function" scope; otherwise, the
    database will have "session" scope. 
    """
    if config.getoption('--func-db', None):
        return 'function'

    return 'session'


@pytest.fixture(scope=db_scope)
def db():
    """CardsDB object connected to a temporary database."""
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
