import pytest


@pytest.mark.xfail
def test_membership():
    assert 1 in [2, 3, 4]
