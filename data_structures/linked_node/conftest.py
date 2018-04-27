from .node import Node
from pytest import fixture


@fixture
def new_node():
    return Node(None)


@fixture
def chained_node():
    return Node(1, Node(2, Node(3)))


@fixture
def loop_node():
    end = Node(4)
    node = Node(1, Node(2, Node(3, Node(2, Node(1, end)))))
    end.next = node.next
    return node
