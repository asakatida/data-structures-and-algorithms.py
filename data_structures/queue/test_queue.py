import pytest


def test_empty_queue_default(new_queue):
    assert new_queue.head is None


def test_empty_queue_dequeue(new_queue):
    with pytest.raises(IndexError):
        new_queue.dequeue()


def test_data_queue_dequeue(ordered_queue):
    assert ordered_queue.dequeue() == 3
    assert ordered_queue.dequeue() == 6


def test_empty_queue_enqueue(new_queue):
    new_queue.enqueue(0)
    assert new_queue.head.value == 0
