from pathlib import Path
from tempfile import TemporaryDirectory
import cards


# This code has some issues when writing a test:
# - We must setup the database **before** testing `count()`
# - We must call `db.close()` **before** we call `assert` (to prevent
#   failing to close the database if the test fails).
#
# These problems can all be addressed with a pytest fixture.
def test_empty():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        count = db.count()
        db.close()

        assert count == 0
