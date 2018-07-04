from data_structures.binary_search_tree.bst import BST
from pytest import fixture


@fixture
def new_bst():
    return BST()


@fixture
def filled_bst():
    return BST([4, 3, 2, 1, 8, 6, 12, 9])


@fixture
def left_bst():
    return BST(range(9, -9, -2))


@fixture
def right_bst():
    return BST(range(-9, 9, 3))
