def test_empty_list_length(new_list):
    assert len(new_list) == 0
    assert new_list.head is None


def test_empty_list_insert(new_list):
    new_list.insert(1)
    assert new_list.head is not None
