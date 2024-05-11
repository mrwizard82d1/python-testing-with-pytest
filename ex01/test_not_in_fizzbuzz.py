import pytest


@pytest.mark.xfail(strict=True)
def test_not_in_fizz_buzz():
    assert 'fizz' not in 'fizzbuzz'
