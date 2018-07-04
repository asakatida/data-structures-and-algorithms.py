from .stack import Stack
from pytest import fixture


@fixture
def new_stack():
    return Stack()


@fixture
def ordered_stack():
    return Stack(range(3, 40, 3))


@fixture
def unordered_stack():
    return Stack(map(lambda i: i % 7, range(73, 40, -2)))


@fixture
def large_stack():
    return Stack("task" for _ in range(0xFFFFFF))
