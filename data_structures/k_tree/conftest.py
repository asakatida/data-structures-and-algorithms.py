from .k_tree import KTree
import pytest


@pytest.fixture
def new_k_tree():
    return KTree()


@pytest.fixture
def filled_k_tree():
    k_tree = KTree()
    return k_tree
