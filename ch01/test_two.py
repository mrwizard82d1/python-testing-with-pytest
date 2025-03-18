import pytest


@pytest.mark.xfail()
def test_failing():
    assert (1, 2, 3) == (1, 2, 3.000001)
