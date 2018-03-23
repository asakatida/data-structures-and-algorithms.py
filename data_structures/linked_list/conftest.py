from .linked_list import LinkedList
from .node import Node
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


@pytest.fixture
def new_node():
    return Node(None)


@pytest.fixture
def chained_node():
    return Node(1, Node(2, Node(3)))
