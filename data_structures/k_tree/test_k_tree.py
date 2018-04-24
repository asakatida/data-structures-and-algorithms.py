def test_empty_bst_length(new_k_tree):
    assert len(new_k_tree) == 0
    assert new_k_tree.root is None


def test_data_bst_contains(filled_k_tree):
    assert 12 in filled_k_tree
    assert (7 in filled_k_tree) is False
    assert 6 in filled_k_tree
    assert 1 in filled_k_tree


def test_empty_bst_insert(new_k_tree):
    new_k_tree.insert(1)
    assert new_k_tree.root is not None
    assert 1 in new_k_tree


def test_data_bst_has_length(filled_k_tree):
    assert len(filled_k_tree) > 0


def test_data_bst_insert_changes_length(filled_k_tree):
    start_len = len(filled_k_tree)
    filled_k_tree.insert(-1)
    filled_k_tree.insert(-2)
    assert len(filled_k_tree) - start_len == 2
    assert -2 in filled_k_tree


def test_data_bst_insert_negative_left(filled_k_tree):
    filled_k_tree.insert(-1)
    assert filled_k_tree.root.left.left.left.left.value == -1


def test_data_bst_in_order_traverse(filled_k_tree):
    lst = []
    filled_k_tree.in_order(lst.append)
    assert lst == [1, 2, 3, 4, 6, 8, 9, 12]


def test_data_bst_pre_order_traverse(filled_k_tree):
    lst = []
    filled_k_tree.pre_order(lst.append)
    assert lst == [4, 3, 2, 1, 8, 6, 12, 9]


def test_data_bst_post_order_traverse(filled_k_tree):
    lst = []
    filled_k_tree.post_order(lst.append)
    assert lst == [1, 2, 3, 6, 9, 12, 8, 4]
