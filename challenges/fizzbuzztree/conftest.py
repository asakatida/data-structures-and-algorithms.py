from data_structures.binary_search_tree.bst import BST
from pytest import fixture


@fixture
def new_bst():
    return BST()


@fixture
def filled_bst():
    return BST([4, 3, 2, 1, 8, 6, 12, 9])


@fixture
def fizz_buzz_bst():
    return BST([15, 3, 5, 0, 45, 30, 7])
