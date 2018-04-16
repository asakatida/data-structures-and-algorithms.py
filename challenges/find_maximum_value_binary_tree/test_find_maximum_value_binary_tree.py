from .find_maximum_value_binary_tree import find_maximum_value


def test_empty_bst_breadth_first(new_bst):
    assert find_maximum_value(new_bst) is None


def test_filled_bst_breadth_first(filled_bst):
    assert find_maximum_value(filled_bst) == 12


def test_left_bst_breadth_first(left_bst):
    assert find_maximum_value(left_bst) == 9


def test_right_bst_breadth_first(right_bst):
    assert find_maximum_value(right_bst) == 6
