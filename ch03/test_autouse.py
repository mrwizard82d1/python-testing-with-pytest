import datetime
import time

import pytest


@pytest.fixture(autouse=True, scope='session')
def footer_session_scope():
    """Report the time at the end of a session."""
    yield
    
    now = datetime.datetime.now()
    print('--')
    print(f'finished: {now.isoformat(timespec='seconds')}')
    print('----------')


@pytest.fixture(autouse=True)
def footer_function_scope():
    """Report test durations after each function."""
    start = datetime.datetime.now()

    yield

    stop = datetime.datetime.now()
    delta = stop - start
    print(f'\ntest duration: {delta.total_seconds()} seconds')


def test_1():
    """Simulate a long-ish running test."""
    time.sleep(1)


def test_2():
    """Simulate a slightly longer test."""
    time.sleep(1.23)
