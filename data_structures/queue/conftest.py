from .queue import Queue
import pytest


@pytest.fixture
def new_queue():
    return Queue()


@pytest.fixture
def ordered_queue():
    return Queue(range(3, 40, 3))


@pytest.fixture
def unordered_queue():
    return Queue(map(lambda i: i % 7, range(73, 40, -2)))


@pytest.fixture
def large_queue():
    return Queue('task' for _ in range(0xFFFFFF))
