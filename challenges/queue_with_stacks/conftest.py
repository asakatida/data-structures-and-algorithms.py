from .queue_with_stacks import Queue
from pytest import fixture


@fixture
def new_queue():
    return Queue()


@fixture
def ordered_queue():
    queue = Queue()
    set(map(queue.enqueue, range(3, 40, 3)))
    return queue


@fixture
def unordered_queue():
    queue = Queue()
    set(map(queue.enqueue, map(lambda i: i % 7, range(73, 40, -2))))
    return queue


@fixture
def large_queue():
    queue = Queue()
    set(map(queue.enqueue, range(0xFFFFFF)))
    return queue
