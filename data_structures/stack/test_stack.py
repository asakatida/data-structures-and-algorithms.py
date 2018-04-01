import pytest


def test_empty_stack_default(new_stack):
    assert new_stack.head is None


def test_empty_stack_pop(new_stack):
    with pytest.raises(IndexError):
        new_stack.pop()


def test_empty_stack_has_size(new_stack):
    assert len(new_stack) == 0


def test_data_stack_pop_changes_size(ordered_stack):
    assert len(ordered_stack) == 13
    assert ordered_stack.pop() == 39
    assert len(ordered_stack) == 12


def test_data_stack_pop(ordered_stack):
    assert ordered_stack.pop() == 39
    assert ordered_stack.pop() == 36


def test_data_stack_pop_exaust(ordered_stack):
    while ordered_stack:
        ordered_stack.pop()
    assert len(ordered_stack) == 0
    with pytest.raises(IndexError):
        ordered_stack.pop()


def test_unordered_pop(unordered_stack):
    assert unordered_stack.pop() == 6
    assert unordered_stack.pop() == 1
    assert unordered_stack.pop() == 3
    assert unordered_stack.pop() == 5


def test_empty_stack_push(new_stack):
    new_stack.push(0)
    assert new_stack.head.value == 0


def test_empty_stack_push_multiple(new_stack):
    for _ in range(30):
        new_stack.push(0)
    new_stack.push(1)
    assert len(new_stack) == 31
    assert new_stack.pop() == 1


def test_empty_stack_push_changes_size(new_stack):
    assert len(new_stack) == 0
    new_stack.push('test')
    assert len(new_stack) == 1
