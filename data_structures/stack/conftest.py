from .stack import Stack
import pytest


@pytest.fixture
def new_stack():
    return Stack()


@pytest.fixture
def ordered_stack():
    return Stack(range(3, 40, 3))


@pytest.fixture
def unordered_stack():
    return Stack(map(lambda i: i % 7, range(73, 40, -2)))


@pytest.fixture
def large_stack():
    return Stack('task' for _ in range(0xFFFFFF))
