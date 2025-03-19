import pytest


@pytest.fixture(name='ultimate_answer')
def ultimate_answer_fixture():
    return 42


def test_everthing(ultimate_answer):
    assert ultimate_answer == 42
