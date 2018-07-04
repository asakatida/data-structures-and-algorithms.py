from .queue import Queue
from pytest import fixture


@fixture
def new_queue():
    return Queue()


@fixture
def ordered_queue():
    return Queue(range(3, 40, 3))


@fixture
def unordered_queue():
    return Queue(map(lambda i: i % 7, range(73, 40, -2)))


@fixture
def large_queue():
    return Queue("task" for _ in range(0xFFFFFF))
