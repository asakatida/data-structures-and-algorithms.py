import pytest


def test_empty_queue_dequeue(new_queue):
    with pytest.raises(IndexError):
        new_queue.dequeue()


def test_empty_queue_has_size(new_queue):
    assert len(new_queue) == 0


def test_data_queue_dequeue_changes_size(ordered_queue):
    assert len(ordered_queue) == 13
    assert ordered_queue.dequeue() == 'dog'
    assert len(ordered_queue) == 12


def test_data_queue_dequeue(ordered_queue):
    assert ordered_queue.dequeue() == 'dog'
    assert ordered_queue.dequeue() == 'dog'


def test_data_queue_dequeue_exaust(ordered_queue):
    while ordered_queue:
        ordered_queue.dequeue()
    assert len(ordered_queue) == 0
    with pytest.raises(IndexError):
        ordered_queue.dequeue()


def test_unordered_dequeue(unordered_queue):
    assert unordered_queue.dequeue() == 'cat'
    assert unordered_queue.dequeue() == 'dog'
    assert unordered_queue.dequeue() == 'cat'
    assert unordered_queue.dequeue() == 'cat'


def test_empty_queue_enqueue_multiple(new_queue):
    for _ in range(30):
        new_queue.enqueue(0)
    new_queue.enqueue(1)
    assert len(new_queue) == 31
    assert new_queue.dequeue() == 0


def test_empty_queue_enqueue_changes_size(new_queue):
    assert len(new_queue) == 0
    new_queue.enqueue('cat')
    assert len(new_queue) == 1
