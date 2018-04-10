from .breadth_first_traversal import breadth_first_traversal


def test_empty_bst_breadth_first(new_bst):
    breadth_first_traversal(new_bst)


def test_filled_bst_breadth_first(filled_bst):
    breadth_first_traversal(filled_bst)


def test_left_bst_breadth_first(left_bst):
    breadth_first_traversal(left_bst)


def test_right_bst_breadth_first(right_bst):
    breadth_first_traversal(right_bst)


def test_right_bst_breadth_first_ordering(right_bst):
    lst = []
    right_bst.breadth_first_traversal(lst.append)
    assert lst == list(range(-9, 9, 3))
