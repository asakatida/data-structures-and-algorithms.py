import pytest


def test_empty_queue_default(new_queue):
    assert new_queue.head is None


def test_empty_queue_dequeue(new_queue):
    with pytest.raises(IndexError):
        new_queue.dequeue()


def test_empty_queue_enqueue(new_queue):
    new_queue.enqueue(0)
    assert new_queue.head.value == 0
