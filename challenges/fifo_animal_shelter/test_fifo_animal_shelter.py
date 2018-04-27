from .fifo_animal_shelter import Cat, Dog
from pytest import raises


def test_empty_queue_dequeue(new_queue):
    with raises(IndexError):
        new_queue.dequeue()


def test_empty_queue_has_size(new_queue):
    assert len(new_queue) == 0


def test_data_queue_dequeue_changes_size(ordered_queue):
    assert len(ordered_queue) == 13
    assert isinstance(ordered_queue.dequeue(), Dog)
    assert len(ordered_queue) == 12


def test_data_queue_dequeue(ordered_queue):
    assert isinstance(ordered_queue.dequeue(), Dog)
    assert isinstance(ordered_queue.dequeue(), Dog)


def test_data_queue_dequeue_exaust(ordered_queue):
    while ordered_queue:
        ordered_queue.dequeue()
    assert len(ordered_queue) == 0
    with raises(IndexError):
        ordered_queue.dequeue()


def test_unordered_dequeue(unordered_queue):
    assert isinstance(unordered_queue.dequeue(), Cat)
    assert isinstance(unordered_queue.dequeue(), Dog)
    assert isinstance(unordered_queue.dequeue(), Cat)
    assert isinstance(unordered_queue.dequeue(), Cat)


def test_empty_queue_enqueue_multiple(new_queue):
    for _ in range(30):
        new_queue.enqueue(Cat())
    new_queue.enqueue(Dog())
    assert len(new_queue) == 31
    assert isinstance(new_queue.dequeue(), Cat)
    assert isinstance(new_queue.dequeue(Dog), Dog)


def test_empty_queue_enqueue_changes_size(new_queue):
    assert len(new_queue) == 0
    new_queue.enqueue(Cat())
    assert len(new_queue) == 1
