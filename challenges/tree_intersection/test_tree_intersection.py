from .tree_intersection import tree_intersection


def test_empty_trees():
    assert tree_intersection() == set()
