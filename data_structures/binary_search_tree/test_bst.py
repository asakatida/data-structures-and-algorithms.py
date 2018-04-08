def test_empty_list_length(new_bst):
    assert len(new_bst) == 0
    assert new_bst.root is None


def test_empty_list_insert(new_bst):
    new_bst.insert(1)
    assert new_bst.root is not None


def test_data_list_has_length(filled_bst):
    assert len(filled_bst) > 0


def test_data_list_insert_changes_length(filled_bst):
    start_len = len(filled_bst)
    filled_bst.insert(-1)
    filled_bst.insert(-2)
    assert len(filled_bst) - start_len == 2
