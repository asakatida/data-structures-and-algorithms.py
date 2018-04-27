from .linked_list import LinkedList
import pytest


@pytest.fixture
def new_list():
    return LinkedList()


@pytest.fixture
def ordered_list():
    return LinkedList(range(3, 40, 3))


@pytest.fixture
def unordered_list():
    return LinkedList(tuple(map(lambda i: i % 7, range(73, 40, -2))))
