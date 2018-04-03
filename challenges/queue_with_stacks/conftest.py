from .queue_with_stacks import Queue
import pytest


@pytest.fixture
def new_queue():
    return Queue()


@pytest.fixture
def ordered_queue():
    queue = Queue()
    set(map(queue.enqueue, range(3, 40, 3)))
    return queue


@pytest.fixture
def unordered_queue():
    queue = Queue()
    set(map(queue.enqueue, map(lambda i: i % 7, range(73, 40, -2))))
    return queue


@pytest.fixture
def large_queue():
    queue = Queue()
    set(map(queue.enqueue, range(0xFFFFFF)))
    return queue
