def test_empty_list_length(new_list):
    assert len(new_list) == 0
    assert new_list.head is None


def test_empty_list_insert(new_list):
    new_list.insert(1)
    assert new_list.head is not None


def test_data_list_insert(ordered_list):
    assert ordered_list.head.value == 3
    ordered_list.insert(7)
    assert ordered_list.head.value == 7
    ordered_list.insert(10)
    assert ordered_list.head.value == 10
