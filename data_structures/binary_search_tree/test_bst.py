def test_empty_bst_length(new_bst):
    assert len(new_bst) == 0
    assert new_bst.root is None


def test_empty_bst_insert(new_bst):
    new_bst.insert(1)
    assert new_bst.root is not None


def test_data_bst_has_length(filled_bst):
    assert len(filled_bst) > 0


def test_data_bst_insert_changes_length(filled_bst):
    start_len = len(filled_bst)
    filled_bst.insert(-1)
    filled_bst.insert(-2)
    assert len(filled_bst) - start_len == 2


def test_data_bst_in_order_traverse(filled_bst):
    lst = []
    filled_bst.in_order(lst.append)
    assert lst == []


def test_data_bst_pre_order_traverse(filled_bst):
    lst = []
    filled_bst.pre_order(lst.append)
    assert lst == []


def test_data_bst_post_order_traverse(filled_bst):
    lst = []
    filled_bst.post_order(lst.append)
    assert lst == []
