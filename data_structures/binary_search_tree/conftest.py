from .bst import BST
from pytest import fixture


@fixture
def new_bst():
    return BST()


@fixture
def filled_bst():
    return BST(i for j in range(4, 0, -1) for i in range(j, j * 4, j))
